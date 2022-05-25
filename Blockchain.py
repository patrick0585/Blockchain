'''
    Blockchain module
'''
from Block import Block
from time import time

class Blockchain:

    def __init__(self):
        self.pending_transactions = []
        self.chain = []
        self.difficulty = 4
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, "Genesis-Block", time(), 0)
        genesis_block.hash = genesis_block.compute_hash()
        self.chain.append(genesis_block)

    @property
    def last_block(self):
        return self.chain[-1]

    def mine(self):

        if not self.pending_transactions:
            return False

        last_block = self.last_block
        block = Block(index=last_block.index + 1,
                    transactions=self.pending_transactions,
                    timestamp=time(),
                    previous_hash=last_block.hash
        )

        block.proof_of_work(difficulty=self.difficulty)

        if last_block.hash != block.previous_hash:
            print(last_block.hash)
            print(block.previous_hash)
            return False
        
        if not self.validate_proof(block):
            return False
        
        self.chain.append(block)


    def validate_proof(self, block):
        print(block.hash)
        print(block.compute_hash())
        print(block.compute_hash())
        return (block.hash.startswith('0' * self.difficulty))

    def new_transaction(self, sender, recipient, amount):
        transaction = {
            'sender' : sender,
            'recipient' : recipient,
            'amount' : amount
        }
        self.pending_transactions.append(transaction)
    
