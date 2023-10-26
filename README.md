# lexiconundrum documentation

## Endpoints

#### GET /search

Gets all words from the dictionary as json.

```curl -X GET https://lexiconundrum.pythonanywhere.com/search```

Response:

```
[{
    "word": "sphygmomanometrically",
    "definition": "obtained with a sphygmomanometer",
    "origin": "Greek (sphygmo-)",
    "partOfSpeech": "adjective",
    "phonetics": "-ˌman-ə-ˈme-trik"
},
{
    ....
}]
```

#### GET /random

Gets one random entry from the dictionary

`curl -X GET https://lexiconundrum.pythonanywhere.com/random`

Response:

`{
    "word": "sphygmomanometrically",
    "definition": "obtained with a sphygmomanometer",
    "origin": "Greek (sphygmo-)",
    "partOfSpeech": "adjective",
    "phonetics": "-ˌman-ə-ˈme-trik"
}`


Filters & Query Parameters
Limit (search only)
In search endpoint, sets a maximum number of entries returned.

Example:

curl -X GET https://lexiconundrum.pythonanywhere.com/random?limit=10
Filter by word content
Filter /search results and /random pool by substrings. Possible parameter names are 'contains', 'startsWith', and 'endsWith'.

Example 1:

curl -X GET https://lexiconundrum.pythonanywhere.com/search?contains=anti
Example 2:

curl -X GET https://lexiconundrum.pythonanywhere.com/random?startsWith=anti&endsWith=ly
Filter by word length
Filter /search results and /random pool by substrings. Possible parameter names are 'length', 'maxLength', and 'minLength'. Parameter 'length' sets a strict equality, while 'maxLength' and 'minLength' set upper and lower bounds for word length.

Example 1:

curl -X GET https://lexiconundrum.pythonanywhere.com/random?length=15
Example 2:

curl -X GET https://lexiconundrum.pythonanywhere.com/search?minLength=10&maxLength=18
Filter by part of speech
Filer /search results and /random pool by part of speech. Acceptable arguments include: 'noun', 'adjective', 'verb', and 'adverb'.

Example:

curl -X GET https://lexiconundrum.pythonanywhere.com/random?partOfSpeech=noun
