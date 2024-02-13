#!/bin/bash

# MySQL credentials
MYSQL_USER="root"
MYSQL_PASSWORD="your_password"

# Command to list databases
MYSQL_COMMAND="mysql -u$MYSQL_USER -p$MYSQL_PASSWORD -e 'show databases;'"

# Execute the command
eval $MYSQL_COMMAND
