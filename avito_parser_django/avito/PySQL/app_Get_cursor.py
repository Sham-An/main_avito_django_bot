import psycopg2


class PostgreSQLConnection:
    def __init__(self, host, port, dbname, user, password):
        self.host = host
        self.port = port
        self.dbname = dbname
        self.user = user
        self.password = password
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                host=self.host,
                port=self.port,
                dbname=self.dbname,
                user=self.user,
                password=self.password
            )

            self.cursor = self.connection.cursor()
            print("Connected to PostgreSQL!")
        except (Exception, psycopg2.Error) as error:
            print("Error connecting to PostgreSQL:", error)

    def execute_query(self, query):
        try:
            self.cursor.execute(query)
            print("Query executed successfully!")
        except (Exception, psycopg2.Error) as error:
            print("Error executing query:", error)

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
            print("Connection closed.")
