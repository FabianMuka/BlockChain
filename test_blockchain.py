from blockchain import Blockchain

# Create a new blockchain
my_blockchain = Blockchain()

# Add some blocks to the blockchain
my_blockchain.add_block("Second block")
my_blockchain.add_block("Third block")

# Print the blockchain
my_blockchain.print_chain()
