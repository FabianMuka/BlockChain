from block import Block

# Create a new block
block1 = Block(index=1, data="First block", previous_hash="0")
block2 = Block(index=2, data="Second block", previous_hash=block1.hash)

# Print the blocks to check if everything is working
print(block1)
print(block2)
