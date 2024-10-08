# -*- coding: utf-8 -*-
"""
Created on Tue Oct 8 09:27:05 2024

@author: youmisuk
"""

First Steps with Python to Interact with a Relational Database

PURPOSE
1. Create a lightweight database using SQLite, which is 
   serverless and open source.

2. Use Python to interface with the database, including:
    - creating a table
    - inserting records into the table
    - querying the data
-----------------------------------------------------------

Learn about SQLite here:
https://www.sqlite.org/about.html


Download SQLite here:
https://www.sqlite.org/download.html

   Windows users will install:
   sqlite-tools-win32-x86-3460100.zip

   Mac users will install:
   sqlite-tools-osx-x86-3460100.zip

After install, launch terminal (Windows users use CMD)
From terminal, cd to sqlite

For example on my Mac machine, I put it here:
/Users/ys2952/sqlite

At prompt, create db called stocks
> sqlite3 stocks.db

You will see something like this:
SQLite version 3.38.2 2022-03-26 13:51:10
Enter ".help" for usage hints.

List the databases like this:
sqlite> .databases

You should see stocks.db listed. For example, I see:
main: /Users/ys2952/sqlite/stocks.db r/w

Next, we will work in Python
------------------------------------------------------------------
# python
import sqlite3

# create some data
stocks = [
        ('NVDA',219,-3.42),
        ('AAPL',146,-2.73),
        ('GOOG',2829.27,-58.20)]


# connect to db

# update with your path to the database
path_to_db = "/Users/ys2952/sqlite/stocks.db"    

# create db connection
conn = sqlite3.connect(path_to_db)

# create cursor
cur = conn.cursor()

# create a table in the db called "holdings" and pass a schema
# end the transaction with a commit
cur.execute('create table holdings (ticker text, price real, chg real)')
conn.commit()

# insert multiple records of data with executemany()
cur.executemany('insert into holdings values (?,?,?)', stocks)
conn.commit()

# query the table
# print all the rows
for row in conn.execute('select * from holdings'):
    print(row)

# print all the rows where price > 200
for row in conn.execute('select * from holdings where price > 200'):
    print(row)

# print all the rows where price > 200. show only ticker, price
for row in conn.execute('select ticker, price from holdings where price > 200'):
    print(row)

# save the resultant dataset in a list
data = []
for row in conn.execute('select ticker, price from holdings where price > 200'):
    data.append(row)

# TRY FOR YOURSELF 
# Create a dataframe with columns: ticker, price.
# Load all of the data into the dataframe


------------------------------------------------------------------
Lastly, we revisit SQLite

List the tables
sqlite> .tables
holdings

Select all data from holdings. Notice queries end with ;
sqlite> select * from holdings;
NVDA|219.0|-3.42
AAPL|146.0|-2.73
GOOG|2829.27|-58.2


TRY FOR YOURSELF 
Write a query that returns all rows where chg > -3.

Exit SQLite
sqlite> .q
------------------------------------------------------------------
