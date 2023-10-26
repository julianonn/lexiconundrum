from flask import Flask, jsonify, request, render_template
from markupsafe import Markup
import pymysql.cursors
import os
import random

app = Flask(__name__)

# Define a route for searching words
@app.route('/', methods=['GET'])
def hello():
    return render_template("index.html")

@app.route('/search', methods=['GET'])
def search_words():

    contains = request.args.get('contains', default='', type=str)
    starts_with = request.args.get('startsWith', default='', type=str)
    ends_with = request.args.get('endsWith', default='', type=str)
    length = request.args.get('length', default='', type=int)
    max_length = request.args.get('maxLength', default='', type=int)
    min_length = request.args.get('minLength', default='', type=int)
    part_of_speech = request.args.get('partOfSpeech', default='', type=str)
    limit = request.args.get('limit', default='', type=str)

    query = "SELECT * FROM words WHERE "

    if contains:
        query += f"word LIKE '%{contains}%' AND "
    if starts_with:
        query += f"word LIKE '{starts_with}%' AND "
    if ends_with:
        query += f"word LIKE '%{ends_with}' AND "
    if length:
        query += f"LENGTH(word) = {length} AND "
    if max_length:
        query += f"LENGTH(word) <= {max_length} AND "
    if min_length:
        query += f"LENGTH(word) >= {min_length} AND "
    if part_of_speech:
        query += f"partOfSpeech = '{part_of_speech}' AND "

    if query.endswith('AND '):
        query = query[:-5]  # Remove the trailing "AND"

    if query.endswith('WHERE '):
        query = query[:-7]  # Remove the trailing "AND"

    query += ";"

    # START QUERY
    try:
        connection = pymysql.connect(host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS"),
            database=os.getenv("DB_NAME"),
            cursorclass=pymysql.cursors.DictCursor)
    except Exception as e:
        return jsonify({"message": "Connection failed"})


    with connection:
        with connection.cursor() as cursor:
            try:
                cursor.execute(query)
            except Exception as e:
                return(f"SQL failed to execute")
            try:
                if limit:
                    words = cursor.fetchmany(limit)
                else:
                    words = cursor.fetchall()
            except Exception as e:
                return jsonify({"message": "Fetch failed"})

    if words:
        return jsonify(words)
    else:
        return jsonify({"message": "No words found"})



# Define a route for getting a random word
@app.route('/random', methods=['GET'])
def get_random_word():
    words = search_words().json  # Reuse the search_words function

    if "message" in words:
        return jsonify(words)

    random_word = random.choice(words)
    return jsonify(random_word)



if __name__ == '__main__':
    app.run(debug=False)