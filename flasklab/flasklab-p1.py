import flask
import psycopg2

app = flask.Flask(__name__)

# connect to the stearns database
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


@app.route('/hello')
def my_function():
    return "Hello World!"


@app.route('/display/<word1>/<word2>')
def my_display(word1, word2):
    the_string = "The words are: " + word1 + " and " + word2;
    return the_string


@app.route('/color/<word1>')
def my_color(word1):
    return '<h1 style="color:Red">' + word1 + '</h1>'


@app.route('/add/<num1>/<num2>')
def add(num1, num2):
    sum = int(num1) + int(num2)
    print_sum = "The sum is: " + str(sum)
    return print_sum


def states_data(state):
    conn = connect()

    if conn != None:
        cur = conn.cursor()
    else:
        print("There was a problem connecting to the database")
        exit()

    abbreviation = None
    get_abbr = "SELECT state FROM states WHERE abbreviation = %s"
    cur.execute(get_abbr, [state])
    abbreviation = cur.fetchone()
    
    get_pop = "SELECT population FROM state_pops WHERE state = %s"
    cur.execute(get_pop, abbreviation)
    population = cur.fetchone()

    conn.commit()
    return population


@app.route('/pop/<state>')
def pop(state):
    population = str(states_data(state)) 
    print_pop = "The sum is: " + population
    return print_pop


if __name__ == '__main__':
    # port numbers:
        # 5109
        # 5209
    my_port = 5109
    app.run(host='0.0.0.0', port = my_port)
