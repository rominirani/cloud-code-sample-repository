import os
import logging
import json
from flask import Flask, jsonify, request

app = Flask(__name__)

inventory_items = {"I-1":10, "I-2":20,"I-3":30}

@app.route('/healthy', methods=['GET'])
def healthy():
    return "All Izz Well"

@app.route('/inventory', methods=['GET'])
def inventorylist():
   return jsonify([inventory_items])

@app.route('/inventory/<string:productid>', methods=['GET'])
def inventory(productid):
   qty = inventory_items.get(productid)
   if qty == None:
    app.logger.warning("Received inventory request for incorrect productid:{}".format(productid))
    qty = -1
   return jsonify({'productid':productid,'qty':qty})

if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=True,  port=server_port, host='0.0.0.0')
