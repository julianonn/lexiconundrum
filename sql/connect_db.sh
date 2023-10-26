#!/bin/bash

mysql -h $DB_HOST -u DB_USER '$DB_NAME' -p --local-infile=1