#!/bin/bash

pip install --user python-dotenv

if [ -f .env ] ; then
    rm .env
fi
touch .env

echo "export DB_USER=your_username" >> .env
echo "export DB_PASS=your_password" >> .env
echo "export DB_HOST=your_database_host_uri" >> .env
echo "export DB_NAME=your_database_name" >> .env


set -a; source .env; set +a

exit