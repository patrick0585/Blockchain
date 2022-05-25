'''
    Simple Block class
'''
import hashlib
import json

class Block:

    def __init__(self, index, transactions, timestamp, previous_hash, nonce=0):
        self.hash = ""
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = nonce

    def compute_hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()

    def proof_of_work(self, difficulty):
        found = False
        while not found:
            self.nonce += 1
            self.hash = self.compute_hash()
            if self.hash[0:difficulty] == "0" * difficulty:
                found = True
            