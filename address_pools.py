from web3 import Web3

url_rpc = 'https://sepolia.infura.io/v3/55fc735e73d74dbaa6eb102b0205ffe0'
factory_contract = Web3.to_checksum_address('0xca0dc46CCc25d70583686768928E2103DdD949BE')
factory_abi = """[
	{
		"inputs": [],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"inputs": [],
		"name": "GetPools",
		"outputs": [
			{
				"internalType": "address[]",
				"name": "",
				"type": "address[]"
			},
			{
				"internalType": "address[]",
				"name": "",
				"type": "address[]"
			},
			{
				"internalType": "address[]",
				"name": "",
				"type": "address[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "uniswapFactory",
		"outputs": [
			{
				"internalType": "contract IUniswapV2Factory",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]"""
w3 = Web3(Web3.HTTPProvider(url_rpc))


uni_factory_contract = w3.eth.contract(address=factory_contract, abi=factory_abi)
address_pool, address_token_0, address_token_1 = uni_factory_contract.functions.GetPools().call()

class Pool:
    def __init__(self,address_token_0,address_token_1):
        self.address_token_0 = address_token_0
        self.address_token_1 = address_token_1

    def token0(self):
        print(self.address_token_0())
    def token1(self):
        print(self.address_token_1())

    def get_reserv(self):

class Factory:
    def __init__(self, address_pool):
        self.address_pool = address_pool
        address_pool = []

    def adr_pool(self):
        print(address_pool)



x = Pool(address_token_0,address_token_1)
print(x.address_token_0)

