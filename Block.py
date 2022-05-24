'''
    Block module
'''
import hashlib

class Block:
    prev_hash = None
    nonce = -1
    data = None
    current_hash = None

    def __init__(self, prev_hash, data):
        self.prev_hash = prev_hash
        self.data = data

    def __repr__(self):
        return "Block: {0} (prev. {1})".format(
            self.current_hash,
            self.prev_hash
        )
    
    @property
    def block_string(self):
        return "{0}-{1}-{2}".format(
            self.prev_hash,
            self.data,
            self.nonce
        )
    
    def hash(self):
        return hashlib.sha256(bytes(self.block_string,"utf-8")).hexdigest()

    def mine(self, difficulty):
        found = False
        while not found:
            self.nonce += 1
            self.current_hash = self.hash()
            if self.current_hash[0:difficulty] == "0" * difficulty:
                found = True
            