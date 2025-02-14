import hashlib
import time


class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = time.time()  # current time
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()  # Calculate the hash when the block is created

    def calculate_hash(self):
        # Create a string with block details
        block_string = f'{self.index}{self.timestamp}{self.data}{self.previous_hash}'
        return hashlib.sha256(block_string.encode('utf-8')).hexdigest()

    def __repr__(self):
        return f"Block(index={self.index}, data={self.data}, hash={self.hash}, previous_hash={self.previous_hash})"
