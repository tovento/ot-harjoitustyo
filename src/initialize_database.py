from database_connection import get_database_connection

def initialize_database():
    """Alustaa tietokannan ohjelman käynnistyessä."""
    connection = get_database_connection()

    if not check_table_exist(connection):
        create_tables(connection)

def check_table_exist(connection):
    """Tarkastaa, onko tietokannassa tietokantatauluja.

    Args:
        connection: Tietokantayhteyden Connection-olio.
    """
    cursor = connection.cursor()
    cursor.execute("""
        SELECT name
        FROM sqlite_schema
        WHERE type='table'
        AND name='Books'
        """)
    result1 = cursor.fetchall()
    cursor.execute("""
        SELECT name
        FROM sqlite_schema
        WHERE type='table'
        AND name='BooksToRead'
        """)
    result2 = cursor.fetchall()

    return len(result1) > 0 or len(result2) > 0

def reinitialize_database():
    """Alustaa tietokannan uudelleen. Poistaa tietokantataulut tietokannasta ja
    luo tietokantataulut uudelleen.
    """
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)

def drop_tables(connection):
    """Poistaa kaikki tietokantataulut tietokannasta.

    Args:
        connection: Tietokantayhteyden Connection-olio.
    """
    cursor = connection.cursor()

    cursor.execute("DROP TABLE if exists Books")
    cursor.execute("DROP TABLE if exists BooksToRead")

    connection.commit()

def create_tables(connection):
    """Luo taulut Books ja BooksToRead tietokantaan.

    Args:
        connection: Tietokantayhteyden Connection-olio.
    """
    cursor = connection.cursor()

    cursor.execute("""CREATE TABLE Books (
                        id INTEGER PRIMARY KEY,
                        date TEXT,
                        title TEXT,
                        author TEXT,
                        pages INT,
                        notes TEXT
                      );
                   """)

    cursor.execute("""CREATE TABLE BooksToRead (
                        id INTEGER PRIMARY KEY,
                        description TEXT
                      );
                   """)

    connection.commit()

if __name__ == "__main__":
    reinitialize_database()
