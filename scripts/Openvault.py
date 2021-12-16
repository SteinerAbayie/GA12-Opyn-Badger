"""
The script below is designed to work on kovan, the addresses will need to be updated to work on other testnets
The script is designed to open an opyn vault. Then is deposits tokens in that vault.
Following the deposit it creates a short oToken. Make sure that the expiry date is a unix timestamp that
expires on 8AM. After that the token created is minted using the vault as collateral.
The token can then be sold on Gnosis Safe, Airswap, or Ox.
The script does not sell the token, testnets are fragmented and in theory a counter party is needed.


"""

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

KovanWallet_addr = "0x3d19f325A3fda9495eEEd07A1AD31Ee73fD79175"
wBTC_addr = "0x50570256f0da172a1908207aaf0c80d4b279f303"
OpynUSD_addr = "0x7e6edA50d1c833bE936492BF42C1BF376239E9e2"


def main():
    account = get_account()
    """
    tx opens the vault and sets the currencey that the vault is meant to accept
    To see how operate works, go to IController, the operate function opens vaults, mints tokens,
    It also settles vaults.
    """
    tx = opyn.operate(
        [
            [
                0,
                KovanWallet_addr,
                KovanWallet_addr,
                wBTC_addr,
                10,
                0,
                0,
                "0x",
            ]
        ],
        {"from": account},
    )
    tx.wait(2)
    # tx2 deposits 5wBTC in the vault
    tx2 = opyn.operate(
        [
            [
                5,
                KovanWallet_addr,
                KovanWallet_addr,
                wBTC_addr,
                10,
                500000000,
                0,
                "0x",
            ]
        ],
        {"from": account},
    )
    tx2.wait(2)
    # tx3 creates a shortOtoken that can then be minted by anyone. If the token already exists
    # then an error will be shown. This is where price is set. Currently opyn does not have a "pricing"
    # contract, this means that either off chain computation must be done to make sure that the option is priced
    # appropriatly or price should be pulled from some API or based on another exchange.
    tx3 = oTokenFactory.createOtoken(
        wBTC_addr,  # wBTC
        OpynUSD_addr,  # OpynUSD
        wBTC_addr,  # wBTC
        62100 * 1e6,  # strike price
        1640419200,  # Christmas_Day MUST BE UNIX and SET TO 8AM
        False,
        {"from": account},
    )
    mintedToken_addy = tx3.events["OtokenWhitelisted"]["otoken"]
    print(mintedToken_addy)
    tx3.wait(3)
    # tx4 mints the token and deposits it in your wallet. One token is minted below. Each token represents one
    # unit of the vault. This means tht for our 5BTC vault, 1 otoken has been minted, only 4 more can be minted

    tx4 = opyn.operate(
        [
            [
                1,
                KovanWallet_addr,
                KovanWallet_addr,
                mintedToken_addy,
                10,
                1 * 1e8,
                0,
                "0x",
            ]
        ],
        {"from": account},
    )
