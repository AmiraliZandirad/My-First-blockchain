# 🐼✋  𝔸爪𝒾ⓡⓐℓ𝐢 𝐙𝔞几𝐝Ⓘ  😂👊
import hashlib

def hashGenerater(data):
    result = hashlib.sha256(data.encode())
    return result.hexdigest()

class Block:
    def __init__(self, data, hash, prev_hash) :
        self.data = data
        self.hash = hash
        self.prev_hash = prev_hash

class   MyBlockchain:
    def __init__(self):
        hashLast = hashGenerater('last_gen')
        hashFirst = hashGenerater('first_gen')

        genesis = Block('gen_data', hashFirst, hashLast)
        self.chain = [genesis]

    def add_block(self,data):
        prev_hash = self.chain[-1].hash
        hash = hashGenerater(data+prev_hash)
        block = Block(data,hash,prev_hash)
        self.chain.append(block)

blch =  MyBlockchain()
blch.add_block('A')
blch.add_block('B')
blch.add_block('C')
for block in blch.chain:
    print(block.__dict__)
