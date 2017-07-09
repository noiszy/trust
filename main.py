from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
# @app.route('/test')
# def hello_world():
def hello_world():
    # return 'Hello World!'
    # return render_template('test.html',number_of_results=num)

    # ### to find out about using firebase data within python, https://firebase.google.com/docs/database/admin/retrieve-data
    # print "ok!"
    #
    # # Import database module.
    # from firebase_admin import db
    #
    # print "ok again!"
    #
    # # Get a database reference to our posts
    # # ref = db.reference('server/saving-data/fireblog/posts')
    # ref = db.reference('trust-2e8ba')
    #
    # # Read the data at the posts reference (this is a blocking operation)
    # print(ref.get())

    return render_template('test.html')


if __name__ == '__main__':
    app.run()
