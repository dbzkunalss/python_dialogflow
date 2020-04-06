# import flask dependencies
from flask import Flask, request, make_response, jsonify, render_template
from df_response import *


# initialize the flask app
app = Flask(__name__)
log = app.logger
# default route
@app.route('/')
def index():
    product = ['apple', 'mango', 'banana']
    try:
        return render_template("index.html", product=product)
    except Exception as e:
        return str(e)


# function for responses
def results():
    # build a request object
    req = request.get_json(force=True)

    # fetch action from json
    action = req.get('queryResult').get('action')
    if action == 'getting.started':
        #

        print(reply)

    

    return reply

# create a route for webhook
@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    # return response

    return results()


# run the app
if __name__ == '__main__':

    app.run()
