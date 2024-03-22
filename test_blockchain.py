import unittest
import time
from blockchain import Block, Blockchain  # Make sure to replace 'your_module_name' with the name of your Python file

class TestBlockchain(unittest.TestCase):

    def setUp(self):
        # Initialize the Blockchain before each test
        self.blockchain = Blockchain()

    def test_block_creation(self):
        # Test the addition and validation of a new block
        self.blockchain.add_new_transaction("Sample transaction data")
        initial_length = len(self.blockchain.chain)
        self.blockchain.mine()
        self.assertEqual(len(self.blockchain.chain), initial_length + 1)
        new_block = self.blockchain.last_block
        self.assertTrue(isinstance(new_block, Block))
        self.assertEqual(new_block.index, initial_length)  # Index of the new block should be one more than the initial length

    def test_genesis_block(self):
        # Test the creation of the genesis block
        genesis_block = self.blockchain.chain[0]
        self.assertEqual(genesis_block.index, 0)
        self.assertEqual(genesis_block.previous_hash, '0')

    def test_new_transaction(self):
        # Test adding a new transaction
        initial_length = len(self.blockchain.unconfirmed_transactions)
        self.blockchain.add_new_transaction("Sample transaction data")
        self.assertEqual(len(self.blockchain.unconfirmed_transactions), initial_length + 1)

    def test_mining(self):
        # Test mining a new block with transactions
        self.blockchain.add_new_transaction("Sample transaction data")
        last_block_index = self.blockchain.last_block.index
        self.blockchain.mine()
        self.assertEqual(self.blockchain.last_block.index, last_block_index + 1)

    def test_proof_of_work(self):
        # Test the proof of work algorithm
        last_block = self.blockchain.last_block
        new_block = Block(index=last_block.index + 1,
                          transactions=["Sample transaction data"],
                          timestamp=time.time(),
                          previous_hash=last_block.hash)
        proof = self.blockchain.proof_of_work(new_block)
        self.assertTrue(self.blockchain.is_valid_proof(new_block, proof))
        self.assertTrue(proof.startswith('0000'))

if __name__ == '__main__':
    unittest.main()
