#!/usr / bin / python

# Функция create_tables() создает четыре таблицы в базе данных поставщиков:
# vendors, parts, vendor_parts и part_drawings.
# You’ll need to have a PostgreSQL database created on your server, and you’ll also need a user that has been granted privileges to the database. You can do this in the psql interface using the following commands:
# CREATE DATABASE some_database;
# CREATE USER some_user WITH ENCRYPTED PASSWORD 'mypass';
# GRANT ALL PRIVILEGES ON DATABASE some_database TO some_user;

import psycopg2
# from config import host
from config import host, bd_name, user, password
from config import config
# import the psycopg2 database adapter for PostgreSQL
from psycopg2 import connect, sql

# use a Python UUID for the table's PRIMARY KEY
import uuid

# declare a new PostgreSQL connection object
# conn = connect(
# dbname = "postgres",
# user = "postgres",
# host = '127.0.0.1',
# password = "postgres"
#  )
conn = connect(dbname=bd_name,
               user=user,
               host=host,
               password=password)


# define a function that will execute SQL statements

def execute_sql(ident=None, sstatement=""):
    print("\nexecute_sql() SQL statement:", sstatement)

    # check if SQL statement/query end with a semi-colon
    if sstatement[-1] != ";":
        err = "execute_sql() ERROR: All SQL statements and "
        err = err + "queries must end with a semi-colon."
        print(err)
    else:
        try:
            # have sql.SQL() return a sql.SQL object
            sql_object = sql.SQL(
                # pass SQL string to sql.SQL()
                sstatement
            ).format(
                # pass the identifier to the Identifier() method
                sql.Identifier(ident)
            )

            # pass the psycopg2.sql.SQL object to execute() method
            conn.execute(sql_object)

            # print message if no exceptions were raised
            print("execute_sql() FINISHED")

        except Exception as err:
            print("execute_sql() ERROR:", err)


def drop_table():
    TABLE_NAME = 'categories'
    sql_statement = "DROP TABLE some_table;"
    execute_sql(TABLE_NAME, sql_statement)
    # If the table doesn’t exist, the following response will be returned:

    # execute_sql() SQL statement: DROP TABLE some_table;
    # execute_sql() ERROR: table "some_table" does not exist


def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE vendors (
            vendor_id SERIAL PRIMARY KEY,
            vendor_name VARCHAR(255) NOT NULL
        )
        """,
        """ CREATE TABLE parts (
                part_id SERIAL PRIMARY KEY,
                part_name VARCHAR(255) NOT NULL
                )
        """,
        """
        CREATE TABLE part_drawings (
                part_id INTEGER PRIMARY KEY,
                file_extension VARCHAR(5) NOT NULL,
                drawing_data BYTEA NOT NULL,
                FOREIGN KEY (part_id)
                REFERENCES parts (part_id)
                ON UPDATE CASCADE ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE vendor_parts (
                vendor_id INTEGER NOT NULL,
                part_id INTEGER NOT NULL,
                PRIMARY KEY (vendor_id, part_id),
                FOREIGN KEY (vendor_id)
                    REFERENCES vendors (vendor_id)
                    ON UPDATE CASCADE ON DELETE CASCADE,
                FOREIGN KEY (part_id)
                    REFERENCES parts (part_id)
                    ON UPDATE CASCADE ON DELETE CASCADE
        )
        """)
    conn = None
    try:
        # read the connection parameters
        params = config  # ()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    pass
    #create_tables()
