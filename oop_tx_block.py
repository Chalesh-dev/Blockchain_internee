from web3 import Web3
import pandas


# block_number =
# rpc_url = ""
# w3 = Web3(Web3.HTTPProvider(rpc_url))
#
# # w3.eth.get_code()
class TxMeta(type):
    def __new__(self, class_name, bases, attrs):
    #     # super().__init__(name, bases, dct, attrs)
    #     for item, y in attrs.items():
    #         print(item)
    #     # cls.contract = {}
    #     # cls.account = {}
    # # def categorize_addresses(cls):
    #     for address in cls.from_address:
    #         if w3.eth.get_code(address) == "0x":
    #             cls.contract.append(address)
    #         else:
    #             cls.account.append(address)
    # def


# class Tx(metaclass=TxMeta):
#     def __init__(self, tx_hash):
#         transaction = w3.eth.get_transaction(tx_hash)
#         self.hash = tx_hash
#         self.value = transaction.get('value', None)  #
#         self.from_address = transaction.get('from', None)
#         self.to_address = transaction.get('to', None)  #
#         self.gasPrice = transaction.get('gasPrice', None)  #
#         self.gasLimit = transaction.get('gas', None)  #
#         self.Nonce = transaction.get('nonce', None)  #####
#         self.accessList = transaction.get('accessList', None)
#         self.blockHash = transaction.get('blockHash', None)
#         self.blockNumber = transaction.get('blockNumber', None)
#         self.chainId = transaction.get('chainId', None)  #
#         self.maxFeePerGas = transaction.get('maxFeePerGas', None)  #
#         self.maxPriorityFeePerGas = transaction.get('maxPriorityFeePerGas', None)  #
#         self.input = transaction.get('input', None)  #
#         self.hash = transaction.get('hash', None)
#         self.transactionIndex = transaction.get('transactionIndex', None)
#         self.type = transaction.get('type', None)
#         self.s = transaction.get('s', None)
#         self.v = transaction.get('v', None)
#         self.r = transaction.get('r', None)
#         self.data = transaction.get("data", None)
#
#
# class Tx_contract(Tx):
#     def __init__(self, tx_hash):
#         super().__init__(tx_hash)
#
#
# class Tx_Account(Tx):
#     def __init__(self, tx_hash):
#         super().__init__(tx_hash)
#
#
# class Block:
#     def __init__(self, block_number):
#         _block = w3.eth.get_block(block_number)
#         self.transaction = self.Transact()
#
#     @staticmethod
#     def Transact():
#         while True:
#             try:
#                 tx_list = []
#                 if w3.is_connected():
#                     block = w3.eth.get_block('latest')
#                     transactions = block["transactions"]
#                     for tx_hash in transactions:
#                         tx_list.append(Tx(tx_hash))
#                         return (tx_list)
#             except Exception:
#                 pass


class F(metaclass=TxMeta):
    def __init__(self, a):
        self.A = a


a = F(2)
