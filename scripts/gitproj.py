from brownie import Contract, accounts  # , Settler, SynthSwap
from brownie_tokens import MintableForkToken
from web3 import Web3


def main():

    wBTC_addr = "0x2260fac5e5542a773aa44fbcfedf7c193bc2c599"
    sUSD_addr = "0x57Ab1ec28D129707052df4dF418D58a2D46d5f51"
    sBTC_addr = "0xfE18be6b3Bd88A2D2A7f928d00292E7a9963CfC6"
    registry_addr = "0x58A3c68e2D3aAf316239c003779F71aCb870Ee47"
    # synth_swap = Contract(registry_addr)
    amount = 1
    wBTC = MintableForkToken(wBTC_addr)
    wBTC._mint_for_testing(accounts[0], amount)
    # swap = SynthSwap.deploy(settler, amount, {"from": deployer})

    StableSwap = Contract(registry_addr)

    sBTC = StableSwap.swappable_synth(wBTC_addr)

    into_synth = (
        StableSwap.get_swap_into_synth_amount(wBTC_addr, sBTC_addr, amount) * 0.99
    )
    into_synth_amt = into_synth / (10 ** 10)
    print(f"This is the synth amt: {into_synth_amt}")

    wBTC.approve(StableSwap, amount, {"from": accounts[0]})
    # wBTC.approve(swap, amount, {"from": deployer})
    tx = StableSwap.swap_into_synth(
        wBTC_addr, sUSD_addr, amount, into_synth_amt, {"from": accounts[0]}
    )
    sBTC_from_swap = int(tx.events["TokenExchange"]["tokens_bought"])
    # print(tx.events)
    print(tx.events["TokenUpdate"]["token_id"])
    print((tx.events["TokenUpdate"]["underlying_balance"]) / (10 ** 10))
    print(sBTC_from_swap / (10 ** 10))
    # print(f"Raw first swap amount is : {sBTC_from_swap}")

    # endamt_expected = int(
    #     SynthSwap.get_swap_into_synth_amount(sBTC_addr, sUSD_addr, 0.99 * (10 ** 10))
    #     * 0.99
    # )
    # print(endamt_expected / (10 ** 10))

    # # # StableSwap.swap_from_synth(_token_id: uint256, _to: address, _amount: uint256, _expected: uint256, _receiver: address = msg.sender)
    # # second = swap.swap_from_synth(
    # #     ,sUSD_addr, sBTC_from_swap, endamt_expected, {"from": accounts[0]}
    # # )

    # # print(second.events)
