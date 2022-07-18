from crypt import methods
import os
import logging
from flask import Flask, jsonify, request
import itertools
import threading

iter = itertools.count(start=1,step=1)
app = Flask(__name__)
app.logger.setLevel(logging.INFO)

inventory_items = {"I-1":10, "I-2":20,"I-3":30}

@app.route('/greeting')
def greeting():
    name = request.args.get('name')
    if name == None:
        name = "World"
    name = "Hello {name}".format(name=name)
    
    with threading.Lock():
        value = next(iter)

    return jsonify({'id':value,'content':name})

@app.route('/inventory', methods=['GET'])
def inventorylist():
   return jsonify([inventory_items])

@app.route('/inventory/<string:productid>', methods=['GET'])
def inventory(productid):
   qty = inventory_items.get(productid)
   if qty == None:
    productid='Invalid Product Id'
    qty = 0
    app.logger.warning("Received inventory request for incorrect productid:{}".format(productid))
   return jsonify({'productid':productid,'qty':qty})


if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=True,  port=server_port, host='0.0.0.0')
