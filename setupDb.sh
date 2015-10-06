#!/bin/bash
#We need SQLITE3 installed
sqlite3 books.db " create table ebooks (isbn integer primary key, id int default 0,title varchar(200),date_found datetime default current_timestamp); "
sqlite3 books.db "create table info(last_run datetime);"
echo "New Database called books.db has been created"

