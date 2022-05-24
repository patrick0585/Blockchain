'''
    Simple Python Blockchain
'''
from Block import Block
from Blockchain import Blockchain

if __name__ == "__main__":
    genesis = Block(0, "Genesis")
    chain = Blockchain()

    chain.add(genesis)
    chain.build_block("Block 2")

    for block in chain.blocks:
        print(block)
