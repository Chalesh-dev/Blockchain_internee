import asyncio
import datetime
import threading
from web3 import Web3
from functools import cache
from multiprocessing import Lock, Process, Queue, current_process



# url_rpc = 'http://192.168.88.248:8545/'
url_rpc = 'https://mainnet.infura.io/v3/71a005723e624ad8a197e7cf885771a9'
factory_contract_abi = """[{"inputs":[{"internalType":"address","name":"_feeToSetter","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"token0","type":"address"},{"indexed":true,"internalType":"address","name":"token1","type":"address"},{"indexed":false,"internalType":"address","name":"pair","type":"address"},{"indexed":false,"internalType":"uint256","name":"","type":"uint256"}],"name":"PairCreated","type":"event"},{"constant":true,"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"allPairs","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"allPairsLength","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"}],"name":"createPair","outputs":[{"internalType":"address","name":"pair","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"feeTo","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"feeToSetter","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"getPair","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_feeTo","type":"address"}],"name":"setFeeTo","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_feeToSetter","type":"address"}],"name":"setFeeToSetter","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]"""
pool_abi = """[{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1","type":"uint256"},{"indexed":true,"internalType":"address","name":"to","type":"address"}],"name":"Burn","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1","type":"uint256"}],"name":"Mint","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0In","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1In","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount0Out","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1Out","type":"uint256"},{"indexed":true,"internalType":"address","name":"to","type":"address"}],"name":"Swap","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint112","name":"reserve0","type":"uint112"},{"indexed":false,"internalType":"uint112","name":"reserve1","type":"uint112"}],"name":"Sync","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"constant":true,"inputs":[],"name":"DOMAIN_SEPARATOR","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"MINIMUM_LIQUIDITY","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"PERMIT_TYPEHASH","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"burn","outputs":[{"internalType":"uint256","name":"amount0","type":"uint256"},{"internalType":"uint256","name":"amount1","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"factory","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getReserves","outputs":[{"internalType":"uint112","name":"_reserve0","type":"uint112"},{"internalType":"uint112","name":"_reserve1","type":"uint112"},{"internalType":"uint32","name":"_blockTimestampLast","type":"uint32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_token0","type":"address"},{"internalType":"address","name":"_token1","type":"address"}],"name":"initialize","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"kLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"mint","outputs":[{"internalType":"uint256","name":"liquidity","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"nonces","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"permit","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"price0CumulativeLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"price1CumulativeLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"skim","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"amount0Out","type":"uint256"},{"internalType":"uint256","name":"amount1Out","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"swap","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"sync","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"token0","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"token1","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"}]"""
w3 = Web3(Web3.HTTPProvider(url_rpc))


class Pool1:
    def __init__(self, address):
        self.pool_address = Web3.to_checksum_address(address)
        self.pool_abi = pool_abi
        self.pool_contract = w3.eth.contract(address=self.pool_address, abi=self.pool_abi)
        self.token0 = self.pool_contract.functions.token0().call()
        self.token1 = self.pool_contract.functions.token1().call()

    def get_reserve(self):
        return self.pool_contract.functions.getReserves().call()

    def get_reserve0(self):
        reserves = self.pool_contract.functions.getReserves().call()
        return reserves[0]

    def get_reserve1(self):
        reserves = self.pool_contract.functions.getReserves().call()
        return reserves[1]

    def exchange_rate(self):
        rates = self.get_reserve()
        exchange_rate = rates[0] / rates[1]
        return exchange_rate

    def get_symbol(self):
        symbol = self.pool_contract.functions.symbol().call()
        return symbol


class FactoryContratThread:
    def __init__(self, factory_contract_address):
        self.factory_contract_address = Web3.to_checksum_address(factory_contract_address)
        self.factory_contract_abi = factory_contract_abi
        self.factory_contract = w3.eth.contract(address=self.factory_contract_address, abi=self.factory_contract_abi)
        self.list_pool = []
        self.get_all_pools(self.pair_length())
        #multiprocessing.Pool(processes=5)
    def pair_length(self):
        return self.factory_contract.functions.allPairsLength().call()

    @cache
    def threading_fun_pool(self, item):
        self.list_pool.append(self.factory_contract.functions.allPairs(item).call())


        def get_pool_class_for_item(self, item):
            return Pool1(self.list_pool[item])

    # def get_all_pools(self,pairs_length):
    #     thread_list = []
    #     for item in range(pairs_length):
    #         thread_list.append(threading.Thread(target=self.threading_fun_pool, args=(item,)))
    #         thread_list[item].start()
    #         try:
    #             thread_list[item-32].join()
    #         except:
    #             pass

    @cache
    def get_all_pools(self, length):
        self.list_pool = []
        thread_list = []
        for item in range(length):
            thread_list.append(threading.Thread(target=self.threading_fun_pool, args=(item,)))
            thread_list[item].start()
            try:
                thread_list[item - 32].join()
            except:
                pass


class FactoryContratCache:
    def __init__(self, factory_contract_address):
        self.factory_contract_address = Web3.to_checksum_address(factory_contract_address)
        self.factory_contract_abi = factory_contract_abi
        self.factory_contract = w3.eth.contract(address=self.factory_contract_address, abi=self.factory_contract_abi)
        self.list_pool = []
        a = 500
        self.get_all_pools(a)

    def pair_length(self):
        return self.factory_contract.functions.allPairsLength().call()

    @cache
    def get_single_pool(self, item):
        pool = Pool1(self.factory_contract.functions.allPairs(item).call())
        self.list_pool.append(pool)

    @cache
    def get_all_pools(self, length):
        self.list_pool = []
        for item in range(length):
            self.get_single_pool(item)
class FactoryContratCore:
    def __init__(self, factory_contract_address):
        self.factory_contract_address = Web3.to_checksum_address(factory_contract_address)
        self.factory_contract_abi = factory_contract_abi
        self.factory_contract = w3.eth.contract(address=self.factory_contract_address, abi=self.factory_contract_abi)
        self.list_pool = []
        a = 2
        self.get_all_pools(a)

    def pair_length(self):
        return self.factory_contract.functions.allPairsLength().call()

    @cache
    def get_single_pool(self, item):
        self.list_pool.append(self.factory_contract.functions.allPairs(item).call())
    def get_pool_class_for_item(self, item):
        return Pool1(self.list_pool[item])

    def core(self):
        process = []
        for w in range(5):
            p = Process(target=self.get_single_pool, args=(w,))
            process.append(p)
            p.start()
            for p in process:
                p.join()

    @cache
    def get_all_pools(self, length):
        self.list_pool = []
        for item in range(length):
            self.get_single_pool(item)


    def to_dict(self):
        return {"factory_contract_address":self.factory_contract_address,
                "list_pool":self.list_pool,
                "factory_abi":self.factory_contract_abi}

    # def __repr__(self):
    #     pass
    #
    #
    # def __str__(self):
    #     pass

print(datetime.datetime.now())
x = FactoryContratCore('0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f')
print(datetime.datetime.now())
print(x.to_dict())
#
# for i in range(10):
#     print(x.get_pool_class_for_item(i).token0)
