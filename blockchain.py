import hashlib
import time


class Block:
    def __init__(self, index, data, previous_hash, difficulty=2):
        self.index = index
        self.timestamp = int(time.time())
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()
        self.difficulty = difficulty

    def calculate_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self):
        target = '0' * self.difficulty  # target is a string of 0s based on difficulty
        while self.hash[:self.difficulty] != target:
            self.timestamp = int(time.time())  # Update timestamp for each new try
            self.hash = self.calculate_hash()  # Recalculate hash
            self.data = f"{self.data} - nonce {self.timestamp}"  # Change data slightly to simulate mining
        print(f"Block mined: {self.hash}")


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "Genesis Block", "0")

    def add_block(self, new_block):
        new_block.mine_block()  # This will mine the block before adding it to the chain
        self.chain.append(new_block)

    def print_chain(self):
        for block in self.chain:
            print(
                f"Block(index={block.index}, data={block.data}, hash={block.hash}, previous_hash={block.previous_hash})")

    def is_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.hash != current_block.calculate_hash():
                print(f"Error: The hash of block {i} is incorrect.")
                return False
            if current_block.previous_hash != previous_block.hash:
                print(f"Error: The previous hash of block {i} is incorrect.")
                return False
        return True


if __name__ == "__main__":
    blockchain = Blockchain()

    # Add some blocks
    blockchain.add_block(Block(1, "Second block", blockchain.chain[-1].hash))
    blockchain.add_block(Block(2, "Third block", blockchain.chain[-1].hash))

    # Print the blockchain
    blockchain.print_chain()

    # Validate the blockchain
    print("Is blockchain valid?", blockchain.is_valid())
