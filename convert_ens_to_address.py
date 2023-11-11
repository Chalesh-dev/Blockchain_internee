from web3 import Web3
import web3
from ens.auto import ns
from ens import ENS

url_test = "https://mainnet.infura.io/v3/56874a7305ee478292c3628e2e85db73"
w3 = Web3(Web3.HTTPProvider(url_test))
#ns = ENS.from_web3(w3)
addr = w3.ens.address('fucktheshit-.eth')
print(addr)
