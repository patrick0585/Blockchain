'''
    Blockchain module
'''
from Block import Block

class Blockchain:
    blocks = []
    difficulty = 4

    def __init__(self):
        pass

    def add(self, block):
        block.mine(self.difficulty)
        self.blocks.append(block)
    
    @property
    def last_block(self):
        return self.blocks[-1] if len(self.blocks) else None
    
    def build_block(self, data):
        if self.last_block:
            block = Block(self.last_block.current_hash, data)
            self.add(block)
        else:
            raise Exception("Missing Genesis block")