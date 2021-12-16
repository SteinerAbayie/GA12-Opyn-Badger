from brownie import Contract, accounts, interface, config, network
from brownie.network import account  # , Settler, SynthSwap
from brownie_tokens import MintableForkToken
from web3 import Web3
from scripts.helpful_scripts import get_account
import time

oTokenFactory_addr = "0xb9D17Ab06e27f63d0FD75099d5874a194eE623e2"
opyn = interface.IController(
    config["networks"][network.show_active()]["Controller_addy"]
)
oTokenFactory = interface.IOtokenFactory(
    config["networks"][network.show_active()]["Factory"]
)


def main():
    account = get_account()

    # tx = opyn.operate(
    #     [
    #         [
    #             0,
    #             "0x3d19f325A3fda9495eEEd07A1AD31Ee73fD79175",
    #             "0x3d19f325A3fda9495eEEd07A1AD31Ee73fD79175",
    #             "0x50570256f0da172a1908207aaf0c80d4b279f303",
    #             10,
    #             0,
    #             0,
    #             "0x",
    #         ]
    #     ],
    #     {"from": account},
    # )
    # tx.wait(2)
    # tx2 = opyn.operate(
    #     [
    #         [
    #             5,
    #             "0x3d19f325A3fda9495eEEd07A1AD31Ee73fD79175",
    #             "0x3d19f325A3fda9495eEEd07A1AD31Ee73fD79175",
    #             "0x50570256f0da172a1908207aaf0c80d4b279f303",
    #             10,
    #             500000000,
    #             0,
    #             "0x",
    #         ]
    #     ],
    #     {"from": account},
    # )
    # tx2.wait(2)
    tx3 = oTokenFactory.createOtoken(
        0x50570256F0DA172A1908207AAF0C80D4B279F303,  # wBTC
        0x7E6EDA50D1C833BE936492BF42C1BF376239E9E2,  # OpynUSD
        0x50570256F0DA172A1908207AAF0C80D4B279F303,  # wBTC
        50000,
        1640418525,  # Christmas_Day
        0,
    )
    # tx4 = opyn.operate(
    #     [
    #         [
    #             1,
    #             "0x3d19f325A3fda9495eEEd07A1AD31Ee73fD79175",
    #             "0x3d19f325A3fda9495eEEd07A1AD31Ee73fD79175",
    #             "0x631Fc713EA35cdc5A2A0B18a1430EEd04ba9BbdB",
    #             10,
    #             1 * 1e8,
    #             0,
    #             "0x",
    #         ]
    #     ],
    #     {"from": account},
    # )
    # StableSwap.settle(tokenID, {"from": accounts[0]})
