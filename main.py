from blockchain import Blockchain
from flask import Flask, jsonify, request

blockchain = Blockchain()

blockchain.add_block("First block")
blockchain.add_block("Second block")
blockchain.add_block("Third block")

print(blockchain.get_all_blocks())
print(blockchain.is_chain_valid())


app = Flask(__name__)


@app.route("/mine_block", methods=["GET"])
def mine_block():
    previous_block = blockchain.get_last_block()
    new_block = blockchain.add_block(f"Block {previous_block.index + 1}")
    response = {
        "message": "Congratulations, you just mined a block!",
        "index": new_block.index,
        "timestamp": str(new_block.timestamp),
        "data": new_block.data,
        "previous_hash": new_block.previous_hash,
        "hash": new_block.hash,
    }
    return jsonify(response), 200


@app.route("/get_chain", methods=["GET"])
def get_chain():
    blocks = []

    for b in blockchain.get_all_blocks():
        blocks.append(
            {
                "index": b.index,
                "timestamp": str(b.timestamp),
                "data": b.data,
                "previous_hash": b.previous_hash,
                "hash": b.hash,
            }
        )

    response = {
        "chain": blocks,
        "length": len(blocks),
        "is_valid": blockchain.is_chain_valid(),
    }

    return jsonify(response), 200


@app.route("/is_valid", methods=["GET"])
def is_valid():
    response = {"is_valid": blockchain.is_chain_valid()}
    return jsonify(response), 200


@app.route("/save_chain", methods=["GET"])
def save_chain():
    blockchain.save_chain("blockchain.json")
    response = {"message": "Blockchain saved"}
    return jsonify(response), 200


app.run(host="0.0.0.0", port=5000)
