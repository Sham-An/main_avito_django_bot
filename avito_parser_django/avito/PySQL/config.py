host = '127.0.0.1'
user = 'postgres'
password = 'postgres'
bd_name = 'postgres'
port = '5432'

# config(
# dbname = bd_name,
# user = user,
# host = host,
# password = password
#  )

config = {
    'host': host,
    'user': user,
    'password': password,
    'database': bd_name
}


"""
sql:

CREATE DATABASE realty
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;
"""