from flask import Blueprint, render_template
from models.order import *
from models.current_orders import *

order_blueprint = Blueprint("order", __name__)

'''

ACTION - HTTP VERB - ROUTE(PATH)

Create - POST - /tasks
Read - GET - /tasks/<id>
Update - PUT - /tasks/<id>
Delete - DELETE - /tasks/<id>
Read all - GET - /tasks

'''

@order_blueprint.route("/")
def index():
    return render_template("index.html", title="Josh's Bookshop")

@order_blueprint.route("/orders")
def orders_page():
    return render_template("orders_page.html", title="orders", current_orders = current_orders)

@order_blueprint.route("/orders/<index>")
def individual_order(index):
    return render_template("order.html", title="Your Order", index=current_orders[int(index)], order=current_orders[int(index)])