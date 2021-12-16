from brownie import Contract, accounts, interface, config, network
from brownie.network import account  # , Settler, SynthSwap
from brownie_tokens import MintableForkToken
from web3 import Web3
from scripts.helpful_scripts import get_account
import time

opyn = interface.IController(
    config["networks"][network.show_active()]["Controller_addy"]
)
oTokenFactory = interface.IOtokenFactory(
    config["networks"][network.show_active()]["Factory"]
)


def main():
    account = get_account()

    tx = opyn.operate(
        [
            [
                0,
                "0x3d19f325A3fda9495eEEd07A1AD31Ee73fD79175",
                "0x3d19f325A3fda9495eEEd07A1AD31Ee73fD79175",
                "0x50570256f0da172a1908207aaf0c80d4b279f303",
                10,
                0,
                0,
                "0x",
            ]
        ],
        {"from": account},
    )
    tx.wait(2)
    tx2 = opyn.operate(
        [
            [
                5,
                "0x3d19f325A3fda9495eEEd07A1AD31Ee73fD79175",
                "0x3d19f325A3fda9495eEEd07A1AD31Ee73fD79175",
                "0x50570256f0da172a1908207aaf0c80d4b279f303",
                10,
                500000000,
                0,
                "0x",
            ]
        ],
        {"from": account},
    )
    tx2.wait(2)
    tx3 = oTokenFactory.createOtoken(
        "0x50570256f0da172a1908207aAf0c80d4b279f303",  # wBTC
        "0x7e6edA50d1c833bE936492BF42C1BF376239E9e2",  # OpynUSD
        "0x50570256f0da172a1908207aAf0c80d4b279f303",  # wBTC
        62100 * 1e6,  # strike price
        1640419200,  # Christmas_Day MUST BE UNIX and SET TO 8AM
        False,
        {"from": account},
    )
    mintedToken_addy = tx3.events["OtokenWhitelisted"]["otoken"]
    print(mintedToken_addy)
    tx3.wait(3)
    tx4 = opyn.operate(
        [
            [
                1,
                "0x3d19f325A3fda9495eEEd07A1AD31Ee73fD79175",
                "0x3d19f325A3fda9495eEEd07A1AD31Ee73fD79175",
                mintedToken_addy,
                10,
                1 * 1e8,
                0,
                "0x",
            ]
        ],
        {"from": account},
    )
