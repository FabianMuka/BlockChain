from blockchain import Blockchain, Block


def test_blockchain():
    blockchain = Blockchain()

    # Add blocks to the blockchain
    blockchain.add_block(Block(1, "Second block", blockchain.chain[-1].hash))
    blockchain.add_block(Block(2, "Third block", blockchain.chain[-1].hash))

    # Print blockchain to check if mining has worked
    blockchain.print_chain()

    # Validate the blockchain
    print("Is blockchain valid?", blockchain.is_valid())

    # Modify a block and check validity again
    blockchain.chain[1].data = "Modified block"
    print("Is blockchain valid after modification?", blockchain.is_valid())


if __name__ == "__main__":
    test_blockchain()
