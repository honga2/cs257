# We use the psycopg2 library to help us connec to the Postgres SQL database
# This library is already installed on stearns.mathcs.carleton.edu
import psycopg2


# Connects to the database
def connect():
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="honga2",
        user="honga2",
        password="lion587smile")

    if conn != None:
        return conn
    else:
        print("There was a problem connecting to the database")


# This function sends a query that creates the two tables for the lab
def query():
    conn = connect()

    if conn != None:
        cur = conn.cursor()
    else:
        print("There was a problem connecting to the database")
        exit()

    northfield = '''
        SELECT longitude, latitude
        FROM uscities
        WHERE city = 'Northfield';
        '''
    try:
        cur.execute(northfield)
        conn.commit()
    except:
        print("\'Northfield\' was not found in the database")

    basic_commands = [
        # max population in US
        '''
        SELECT city
        FROM uscities
        WHERE population = (SELECT
                            MAX(population)
                            FROM uscities);
        ''',
        # min population in MN
        '''
        SELECT city
        FROM uscities
        WHERE population = (SELECT
                            MIN(population)
                            FROM uscities
                            WHERE state = 'Minnesota');
        ''',
        # furthest north
        '''
        SELECT city
        FROM uscities
        WHERE latitude = (SELECT
                          MAX(latitude)
                          FROM uscities);
        ''',
        # furthest south
        '''
        SELECT city
        FROM uscities
        WHERE latitude = (SELECT
                          MIN(latitude)
                          FROM uscities);
        ''',
        # furthest east
        '''
        SELECT city
        FROM uscities
        WHERE longitude = (SELECT
                           MAX(longitude)
                           FROM uscities);
        ''',
        # furthest west
        '''
        SELECT city
        FROM uscities
        WHERE longitude = (SELECT
                           MIN(longitude)
                           FROM uscities);
        ''',
    ]

    try:
        for _ in basic_commands:
            cur.execute(_)
        conn.commit()
    except:
        print("Something went wrong... Please verify that your query is valid.")

    return None

def states(input):
    conn = connect()

    if conn != None:
        cur = conn.cursor()
    else:
        print("There was a problem connecting to the database")
        exit()

    if len(input) == 2:
        cur.execute("SELECT state FROM states WHERE abbreviation = ?;", (input))
        result = cur.fetchone()

        cur.execute("SELECT population FROM uscities WHERE city = ?;", (result))
        result2 = cur.fetchall()
        for row in result2:
            print(row[1])


if __name__ == "__main__":
    query()
    input = input("Enter a state: ")
    states(input)

