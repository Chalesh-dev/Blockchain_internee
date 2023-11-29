from web3 import Web3

#Values
uni_factory_address =Web3.to_checksum_address('0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f')
uni_factory_abi = '''[{"inputs":[{"internalType":"address","name":"_feeToSetter","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"token0","type":"address"},{"indexed":true,"internalType":"address","name":"token1","type":"address"},{"indexed":false,"internalType":"address","name":"pair","type":"address"},{"indexed":false,"internalType":"uint256","name":"","type":"uint256"}],"name":"PairCreated","type":"event"},{"constant":true,"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"allPairs","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"allPairsLength","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"}],"name":"createPair","outputs":[{"internalType":"address","name":"pair","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"feeTo","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"feeToSetter","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"getPair","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_feeTo","type":"address"}],"name":"setFeeTo","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_feeToSetter","type":"address"}],"name":"setFeeToSetter","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]'''
pk = '72ab21fee5ceead03a923a2dc171472a0c0180eb88884ba0c7ee650f015f5ec7'
C ='https://mainnet.infura.io/v3/56874a7305ee478292c3628e2e85db73'



w3 = Web3(Web3.HTTPProvider(url_rpc))


def get_uni(token_1, token_2):
    uni_factory_contract = w3.eth.contract(address=uni_factory_address, abi=uni_factory_abi)
    pool = uni_factory_contract.functions.getPair(token_1,token_2).call()
    return pool




def exchange_rate(pool_address,token1, token2):
    pool_abi = [......]
    pool_contract = w3.eth.contract(address=pool_address , abi=pool_abi)
    reserves = pool_contract.functions.getReserves().call()
    reserve_token1 , reserve_token2 = reserves[0] , reserves[1]
    exchange_rate = reserve_token1 / reserve_token2
    return exchange_rate



token_1_address = Web3.to_checksum_address("0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48")
token_2_address = Web3.to_checksum_address("0xdAC17F958D2ee523a2206206994597C13D831ec7")

pool_address = get_uni(token_1_address, token_2_address)
print(pool_address)
