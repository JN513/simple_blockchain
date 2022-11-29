from blockchain import Blockchain

blockchain = Blockchain()

blockchain.add_block("First block")
blockchain.add_block("Second block")
blockchain.add_block("Third block")

print(blockchain.get_all_blocks())
print(blockchain.is_chain_valid())