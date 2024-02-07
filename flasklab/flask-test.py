import flask


app = flask.Flask(__name__)


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
    sum = num1+num2
    print_sum = "The sum is: " + sum;
    return print_sum


if __name__ == '__main__':
    # port numbers:
        # 5109
        # 5209
    my_port = 5109
    app.run(host='0.0.0.0', port = my_port)
