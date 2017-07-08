from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
# @app.route('/test')
# def hello_world():
def hello_world():
    # return 'Hello World!'
    # return render_template('test.html',number_of_results=num)
    return render_template('test.html')


if __name__ == '__main__':
    app.run()
