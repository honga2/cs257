# We use the psycopg2 library to help us connec to the Postgres SQL database
# This library is already installed on stearns.mathcs.carleton.edu
import psycopg2


# This function tests to make sure that you can connect to the database
def test_connection():

    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="honga2",
        user="honga2",
        password="lion587smile")

    if conn is not None:
        print( "Connection Worked!" )
    else:
        print( "Problem with Connection" )

    return None

# This function sends a query that creates the two tables for the lab
def query():

    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="honga2",
        user="honga2",
        password="lion587smile")

    cur = conn.cursor()

    northfield = "SELECT longitude, latitude FROM uscities WHERE city = 'Northfield';"

    try:
        cur.execute(northfield)
        conn.commit()
    except:
        print("\'Northfield\' was not found in the database")

    commands = [
        '''
        SELECT city FROM uscities WHERE population = (SELECT MAX(population)
                                                      FROM uscities);
        ''',
    ]

    try:
        for _ in commands:
            cur.execute(_)
        conn.commit()
    except:
        print("Something went wrong... Please verify that your query is valid.")
    finally:
        cur.close()
        conn.close()

    return None


query()

