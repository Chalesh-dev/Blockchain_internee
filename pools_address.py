from web3 import Web3

url_rpc = 'https://mainnet.infura.io/v3/71a005723e624ad8a197e7cf885771a9'
factory_contract_abi = """[{"inputs":[{"internalType":"address","name":"_feeToSetter","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"token0","type":"address"},{"indexed":true,"internalType":"address","name":"token1","type":"address"},{"indexed":false,"internalType":"address","name":"pair","type":"address"},{"indexed":false,"internalType":"uint256","name":"","type":"uint256"}],"name":"PairCreated","type":"event"},{"constant":true,"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"allPairs","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"allPairsLength","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"}],"name":"createPair","outputs":[{"internalType":"address","name":"pair","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"feeTo","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"feeToSetter","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"getPair","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_feeTo","type":"address"}],"name":"setFeeTo","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_feeToSetter","type":"address"}],"name":"setFeeToSetter","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]"""

w3 = Web3(Web3.HTTPProvider(url_rpc))

class Pool:
    def __init__(self,address):
        self.address
class FactoryContrat:
    def __init__(self, factory_contract_address):
        self.factory_contract_address = Web3.to_checksum_address(factory_contract_address)
        self.factory_contract_abi = factory_contract_abi
        self.factory_contract = w3.eth.contract(address=self.factory_contract_address, abi=self.factory_contract_abi)
        self.list_address_pool = []

    def address_pool(self):
        paris_length = self.factory_contract.functions.allPairsLength().call()
        for item in range(paris_length):
            self.list_address_pool.append(Pool(self.factory_contract.functions.allPairs(item).call()))

    def pai
    def tokens_pool(self, token1, token2):
        self.token1 = token1
        self.token2 = token2
        self.factory_contract.functions.getSeserves().call()


x = FactoryContrat('0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f')
print(x.address_pool())
