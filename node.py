import json
from flask import Flask, send_from_directory
from flask_cors import CORS
from Blockchain import Blockchain

DEBUG = True

app = Flask(__name__)
CORS(app)

blockchain = Blockchain()
blockchain.new_transaction(sender="ALice", recipient="Bob", amount="10 BTC")
blockchain.new_transaction(sender="Bob", recipient="Jimmy", amount="101 BTC")
blockchain.mine()


@app.route('/')
def index():
    return send_from_directory('blockchain-vue-frontend', 'index.html')

@app.route('/blocks', methods=['GET'])
def get_blocks():
    blocks = []
    for b in blockchain.chain:
        blocks.append(b.__dict__)
    return json.dumps(blocks)