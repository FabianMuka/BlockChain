from block import Block


class Blockchain:
    def __init__(self):
        self.chain = []  # List to store blocks
        self.create_genesis_block()  # Create the first block (genesis block)

    def create_genesis_block(self):
        # Manually create the genesis block with index 0 and previous_hash as "0"
        genesis_block = Block(index=0, data="Genesis Block", previous_hash="0")
        self.chain.append(genesis_block)

    def add_block(self, data):
        # Add a new block to the blockchain
        previous_block = self.chain[-1]
        new_block = Block(index=previous_block.index + 1, data=data, previous_hash=previous_block.hash)
        self.chain.append(new_block)

    def print_chain(self):
        for block in self.chain:
            print(block)

    def is_chain_valid(self):
        # Iterate through all blocks in the chain
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Check if the current block's hash is correct
            if current_block.hash != current_block.calculate_hash():
                print(f"Error: The hash of block {current_block.index} is incorrect.")
                return False

            # Check if the previous hash is correct
            if current_block.previous_hash != previous_block.hash:
                print(f"Error: The previous hash of block {current_block.index} is incorrect.")
                return False

        return True
