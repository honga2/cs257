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
def create_tables():

    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="honga2",
        user="honga2",
        password="lion587smile")

    cur = conn.cursor()

    sqltbl1 = '''
        DROP TABLE IF EXISTS uscities;
        CREATE TABLE uscities (
          city text,
          stat text,
          population real,
          latitude real,
          longitude real
        ); '''

    cur.execute( sqltbl1 )

    # sqltbl2 =
    # cur.execute(sqltbl2)

    conn.commit()

    return None


create_tables()

