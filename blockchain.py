from hashlib import sha512
from time import time
from random import randint
from datetime import datetime


class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        hash = ""
        nonce = 1
        while not self.is_hash_valid(hash):
            hash = sha512(
                f"{self.data}:{self.timestamp}:{self.previous_hash}:{self.index}:{nonce}".encode()
            ).hexdigest()
            nonce += 1

        #print(f"Hash found: {hash}")
        print(f"Nonce: {nonce}")
        return hash

    def is_hash_valid(self, hash):
        return hash.startswith("0000")


class Blockchain:
    def __init__(self) -> None:
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis = Block(0, datetime.now(), "Genesis Block", "0")
        self.chain.append(genesis)

    def add_block(self, data):
        last_block = self.get_last_block()
        new_block = Block(last_block.index + 1, datetime.now(), data, last_block.hash)
        self.chain.append(new_block)

    def get_last_block(self):
        return self.chain[-1]

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.previous_hash != previous_block.hash:
                return False

            if not current_block.is_hash_valid(current_block.hash):
                return False

        return True

    def get_all_blocks(self):
        return self.chain

    def check_block(self, index):
        return self.chain[index]

    def check_block_data(self, index):
        return self.chain[index].data
