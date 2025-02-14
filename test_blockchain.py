from blockchain import Blockchain

# Create a new blockchain
my_blockchain = Blockchain()

# Add some blocks to the blockchain
my_blockchain.add_block("Second block")
my_blockchain.add_block("Third block")

# Print the blockchain
my_blockchain.print_chain()

# Validate the blockchain
print("Is blockchain valid?", my_blockchain.is_chain_valid())

# Let's break the chain by changing the data of the second block
my_blockchain.chain[1].data = "Modified block"

# Recalculate the hash for the modified block
my_blockchain.chain[1].hash = my_blockchain.chain[1].calculate_hash()

# Update the previous_hash of the next block
my_blockchain.chain[2].previous_hash = my_blockchain.chain[1].hash

# Recalculate the hash for block 2 to reflect the updated previous_hash
my_blockchain.chain[2].hash = my_blockchain.chain[2].calculate_hash()

# Check the validity again after tampering with the blockchain
print("Is blockchain valid after modification?", my_blockchain.is_chain_valid())
