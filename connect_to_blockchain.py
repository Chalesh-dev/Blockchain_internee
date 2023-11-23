from web3 import Web3

class Tx:
    def __init__(self,hash):
        transaction = w3.eth.get_transaction(tx_hash)
        self.hash = hash
        self.value = transaction['value']

block_number = 18611344
rpc_url = 'https://go.getblock.io/98e8ae2f1d6e441e9d61d41a5f34c50a'
w3 = Web3(Web3.HTTPProvider(rpc_url))
tx_list = []
if w3.is_connected():
    block = w3.eth.get_block('latest')
    if block :
        transactions = block["transactions"]
        for tx_hash in transactions:
            tx_list.append(Tx(transactions))
            # transaction = w3.eth.get_transaction(tx_hash)
            # print("Transaction Hash:", tx_hash)
            # print("From:", transaction["from"])
            # print("To:", transaction["to"])
            # print("Value:", transaction["value"])
            # print("Gas Price:", transaction["gasPrice"])
            # print("Gas Limit:", transaction["gas"])
            # print("Nonce:", transaction["nonce"])
            # print("\n")
        else:
            print("Block not found")
    else:
        print("Erorr connectiong to json rpc server!")
