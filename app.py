# import flask dependencies
from flask import Flask, request, make_response, jsonify, render_template
from df_response import *
from actions import *
from mongoengine import *
from database.db import initialize_db
from database.models import Order

# initialize the flask app
app = Flask(__name__)
log = app.logger

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/orders-db'
}

initialize_db(app)



# default route
@app.route('/')
def index():
    
    try:
        return render_template("index.html", product=products_final )
    except Exception as e:
        return str(e)

# function for responses
def results():
    # build a request object
    req = request.get_json(force=True)
    session = str(req.get('session')).split('/')[-1]
    order_session = Order(session = session)
    if Order.objects(session=session) is None:
        order_session.save()

    # fetch action from json
    action = req.get('queryResult').get('action')
    parameters = req.get('queryResult').get('parameters')
    if action == 'getting.started':
        return {'fulfillmentText': 'webhook works'}

    elif action == 'delivery.product.add' or action == 'delivery.search' or action == 'delivery.order.add':
        reply = add_products(parameters,session)
    elif action == 'delivery.product.remove':
        reply = delete_products(parameters, session)
    elif action == 'delivery.product.swap':
        reply = update_products(parameters, session)
    elif action == 'delivery.order.check':
        reply = check_order()

    return reply

# create a route for webhook
@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    # return response

    return results()


# run the app
if __name__ == '__main__':

    app.run()
