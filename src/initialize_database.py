from database_connection import get_database_connection

def initialize_database():
    """TODO """
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)

def drop_tables(connection):
    """TODO """
    cursor = connection.cursor()

    cursor.execute("DROP TABLE if exists Books")

    connection.commit()

def create_tables(connection):
    """TODO """
    cursor = connection.cursor()

    cursor.execute("""CREATE TABLE Books (
                          id SERIAL PRIMARY KEY,
                          date TEXT,
                          title TEXT,
                          author TEXT,
                          pages INT,
                          notes TEXT
                       );
                   """)

    connection.commit()

if __name__ == "__main__":
    initialize_database()
