import os
import logging
from flask import Flask, jsonify, request
import itertools
import threading

iter = itertools.count(start=1,step=1)
app = Flask(__name__)
app.logger.setLevel(logging.DEBUG)

@app.route('/greeting')
def greeting():
    name = request.args.get('name')
    if name == None:
        name = "World"
    name = "Hello {name}".format(name=name)
    
    with threading.Lock():
        value = next(iter)

    return jsonify({'id':value,'content':name})


if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=True,  port=server_port, host='0.0.0.0')
