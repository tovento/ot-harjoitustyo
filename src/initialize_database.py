from database_connection import get_database_connection

def initialize_database():
    """TODO"""
    connection = get_database_connection()

    if not check_table_exist(connection):
        create_tables(connection)

def check_table_exist(connection):
    """TODO"""
    cursor = connection.cursor()
    cursor.execute("""
        SELECT name
        FROM sqlite_schema
        WHERE type='table'
        AND name='Books'""")
    result = cursor.fetchall()

    return len(result) == 1

def reinitialize_database():
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
    reinitialize_database()
