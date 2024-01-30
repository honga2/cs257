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

    cur.execute(northfield)
    result = cur.fetchone()
    if result is not None:
        print(result)
    else:
        print("\'Northfield\' was not found in the database")

    commands = [
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

    if commands is None:
        print("Something went wrong... Please verify that your query is valid.")

    results = []
    for _ in commands:
        cur.execute(_)
        r = cur.fetchall()
        results.append(r)

    for _ in results:
        print(_)

    conn.commit()
    return None


def states_data(state):
    conn = connect()

    if conn != None:
        cur = conn.cursor()
    else:
        print("There was a problem connecting to the database")
        exit()

    abbreviation = None
    get_abbr = "SELECT state FROM states WHERE abbreviation = %s"
    cities = None
    get_cities = "SELECT city FROM uscities WHERE state = %s"
    if len(state) == 2:
        cur.execute(get_abbr, [state])
        abbreviation = cur.fetchone()
        cur.execute(get_cities, [abbreviation])
        cities = cur.fetchall()
    else:
        cur.execute(get_cities, [state])
        cities = cur.fetchall()

    if cities is None:
        print("Invalid state.")
        exit()

    pops = []
    for city in cities:
        get_pop = "SELECT population FROM uscities WHERE city = %s"
        cur.execute(get_pop, [city])
        population = cur.fetchone()
        pops.append(population)

    for _ in pops:
        print(_)

    conn.commit()
    return None



if __name__ == "__main__":
    query()
    state = input("Enter a state: ")
    states_data(state)

