from web3 import Web3
import pandas as pd

block_number = 18611344
rpc_url = 'https://go.getblock.io/98e8ae2f1d6e441e9d61d41a5f34c50a'
w3 = Web3(Web3.HTTPProvider(rpc_url))

class Tx:
    def __init__(self, tx_hash):
        transaction = w3.eth.get_transaction(tx_hash)
        print(transaction)
        self.hash = tx_hash
        self.value = transaction.get('value', None)  #
        self.from_address = transaction.get('from', None)
        self.to_address = transaction.get('to', None)  #
        self.gasPrice = transaction.get('gasPrice', None)  #
        self.gasLimit = transaction.get('gas', None)  #
        self.Nonce = transaction.get('nonce', None)  #####
        self.accessList = transaction.get('accessList', None)
        self.blockHash = transaction.get('blockHash', None)
        self.blockNumber = transaction.get('blockNumber', None)
        self.chainId = transaction.get('chainId', None)  #
        self.maxFeePerGas = transaction.get('maxFeePerGas', None)  #
        self.maxPriorityFeePerGas = transaction.get('maxPriorityFeePerGas', None)  #
        self.input = transaction.get('input', None)  #
        self.hash = transaction.get('hash', None)
        self.transactionIndex = transaction.get('transactionIndex', None)
        self.type = transaction.get('type', None)
        self.s = transaction.get('s', None)
        self.v = transaction.get('v', None)
        self.r = transaction.get('r', None)
        self.data = transaction.get("data", None)
        self.tx_df = pd.DataFrame(transaction)
    def value_to_ether(self):
        return w3.from_wei(self.value, "ether")

    def send_transaction(self):
        pk = '72ab21fee5ceead03a923a2dc171472a0c0180eb88884ba0c7ee650f015f5ec7'
        acct = w3.eth.account.from_key(pk)
        transaction = {
            'from': acct.address,
            'to': self.to_address,
            'value': self.value,
            'nonce': w3.eth.get_transaction_count(acct.address),
            'gas': self.gasLimit,
            'maxFeePerGas': w3.to_wei(20, "gwei"),
            'maxPriorityFeePerGas': w3.to_wei(2, "gwei"),
            # 'input': self.input,
            'chainId': self.chainId,
        }
        singed = w3.eth.account.sign_transaction(transaction, pk)
        tx_hash = w3.eth.send_raw_transaction(singed.rawTransaction)

        receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        print(receipt)

    def gas_fee(self):
        if self.type == 1:
            return (self.tx_df['gasLimit']) * (self.tx_df['gasPrice'])
        elif self.type == 2:
            return (self.tx_df['maxPriorityFeePerGas']) + (self.tx_df['maxFeePerGas']) * (self.tx_df['gasLimit'])
        else:
            return Exception

class Block:
    def __init__(self ,block_number):
        _block = w3.eth.get_block(block_number)
        self.transaction = self.Transact()
    @staticmethod
    def Transact():
        while True:
            try:
                tx_list = []
                if w3.is_connected():
                    block = w3.eth.get_block('latest')
                    transactions = block["transactions"]
                    for tx_hash in transactions:
                        tx_list.append(Tx(tx_hash))
                        return (tx_list)
            except Exception:
                    pass
    def tx_receipt(self , transaction_receipt):
        for item in self.transaction:
            transaction_receipt = w3.eth.get_transaction_receipt(item.hash)
            return transaction_receipt
    def avg_gas(self):
        gas_list = []
        for item in self.transaction:
            gas_list.append(item.gas_fee())
        return sum(gas_list)/len(gas_list)
