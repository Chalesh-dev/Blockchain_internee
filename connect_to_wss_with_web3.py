import asyncio
from web3 import AsyncWeb3
from web3.providers import WebsocketProviderV2
#
# connection = Web3(Web3.WebsocketProvider("wss://go.getblock.io/79b0cd2e301c4d16a354f2e2d9ee614a"))
# w3 = Web3(Web3.HTTPProvider("https://go.getblock.io/9a02ef186c5d4348b34df813870b2b02"))

async def ws_v2_subscription_context_manager_example():
    async with AsyncWeb3.persistent_websocket(
        WebsocketProviderV2("wss://go.getblock.io/79b0cd2e301c4d16a354f2e2d9ee614a")
    ) as w3:
        # subscribe to new block headers
        subscription_id = await w3.eth.subscribe("newHeads")


        async for response in w3.ws.listen_to_websocket():
            print(f"{response}\n")
            # handle responses here

        # still an open connection, make any other requests and get
        # responses via send / receive
        latest_block = await w3.eth.get_block("latest")
        print(f"Latest block: {latest_block}")

        # the connection closes automatically when exiting the context
        # manager (the `async with` block)

asyncio.run(ws_v2_subscription_context_manager_example())