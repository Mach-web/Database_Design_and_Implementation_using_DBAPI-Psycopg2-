# Database_Design_and_Implementation_using_DBAPI-Psycopg2-
## CIT-223-018/2021 Anderson Macharia Kinyua

## Documentation


This application is a basic implementation of a database before being uploaded to a server such as oracle. 

I have used postgres for my implementation. To instantiate the app, you must have psycopg2 installed in your 

computer. You can use the following command to install psycopg2: pip install psycopg2-binary. Postgres should also 

have been installed. 

Run the following commands in your linux terminal to instantiate the app:

sudo -u postgres -i

pip install psycopg2-binary

dropdb artist

createdb artist

python3 artist.py

#### You can access the database in command line using the following commands

psql artist

SELECT * FROM artists;

SELECT * FROM album;

SELECT * FROM track;


The application creates the tables, inserts the demo data and the fetches and displays the data.

I have attached the some images to show expected results.
