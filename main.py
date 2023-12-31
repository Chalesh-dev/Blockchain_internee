from dataclasses import asdict, dataclass
from pprint import pprint
from typing import Optional
import rlp
from eth_typing import HexStr
from eth_utils import keccak, to_bytes
from rlp.sedes import Binary, big_endian_int, binary
from web3 import Web3
from web3.auto import w3



class Transaction(rlp.Serializable):
    fields = [
        ("nonce", big_endian_int),
        ("gas_price", big_endian_int),
        ("gas", big_endian_int),
        ("to", Binary.fixed_length(20, allow_empty=True)),
        ("value", big_endian_int),
        ("data", binary),
        ("v", big_endian_int),
        ("r", big_endian_int),
        ("s", big_endian_int)
    ]


@dataclass
class DecodedTx:
    hash_tx: str
    from_: str
    to: Optional[str]
    nonce: int
    gas: int
    gas_price: int
    value: int
    data: str
    chain_id: int
    r: str
    s: str
    v: int


def hex_to_bytes(data: str) -> bytes:
    return to_bytes(hexstr=HexStr(data))


def decode_raw_tx(raw_tx: str):
    tx = rlp.decode(hex_to_bytes(raw_tx), Transaction)
    hash_tx = Web3.to_hex(keccak(hex_to_bytes(raw_tx)))
    from_ = w3.eth.account.recover_transaction(raw_tx)
    to = w3.to_checksum_address(tx.to) if tx.to else None
    data = w3.to_hex(tx.data)
    r = hex(tx.r)
    s = hex(tx.s)
    chain_id = (tx.v - 35) // 2 if tx.v % 2 else (tx.v - 36) // 2
    return DecodedTx(hash_tx, from_, to, tx.nonce, tx.gas, tx.gas_price, tx.value, data, chain_id, r, s, tx.v)


def main():
    raw_tx = """0x02f8710118839896808507ed3437908252089464bda0a47b91da383c60f02290678033266427ba8718de76816d800080c001a06152c61fadcba9fff2fe863740eaece160d7e3047814d6f4deffb662875c365fa034f731fca8ab7a9cb4c3c8909a663186004b0fc6798d5cfb034c9e69862021f2"""
    res = decode_raw_tx(raw_tx)
    pprint(asdict(res))


if __name__ == "__main__":
    main()
