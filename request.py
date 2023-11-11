# Run ``pip install websockets`` before importing the library.
import re

import asyncio
import json
from web3 import Web3
#Web3(Web3.WebsocketProvider('wss://go.getblock.io/79b0cd2e301c4d16a354f2e2d9ee614a'))
connection = Web3(Web3.WebsocketProvider("wss://go.getblock.io/79b0cd2e301c4d16a354f2e2d9ee614a"))
w3 = Web3(Web3.HTTPProvider("https://go.getblock.io/9a02ef186c5d4348b34df813870b2b02"))
async def handler():
    async with connection as websocket:
        # Sends a message.
        await websocket.send(
            '{"jsonrpc":"2.0", "id": 1, "method": "eth_subscribe", "params": ["newHeads"]}')

        # Receives the replies.
        async for message in websocket:
            message = json.loads(message)
            # print(message)
            try:
                block_hash = message['params']['result']['hash']
                # print(block_hash)
                trx = w3.eth.get_block(block_hash)
                trx = trx["transactions"]
                print(trx)
                for tx in trx:

                    print(w3.eth.get_raw_transaction(tx))
            except Exception as e:
                print(e)

        # Closes the connection.
        await websocket.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(handler())


# wscat -c wss://mainnet.infura.io/ws/v3/YOUR-API-KEY -x '{"jsonrpc":"2.0", "id": 1, "method": "eth_subscribe", "params": ["newHeads"]}'