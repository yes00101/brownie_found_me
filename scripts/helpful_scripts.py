from brownie import network, config, accounts, MockV3Aggregator
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()

FORKED_LOCAL_ENVIRONMENT = ["mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENT = ["development", "ganache-local"]

DECIMALS = 8
STARTING_PRICE = 200000000000


def get_account():
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENT
        or network.show_active() in FORKED_LOCAL_ENVIRONMENT
    ):
        print(f"account = {accounts[0]}")
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print(f"The active network is {network.show_active()}")
    print("Deoplying Mocks ...")
    if len(MockV3Aggregator) <= 0:
        # MockV3Aggregator.deploy(
        #     DECIMALS, Web3.toWei(STARTING_PRICE, "ether"), {"from": get_account()}
        # )
        MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": get_account()})
