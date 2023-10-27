import os
import json
from web3 import Web3
from loguru import logger
from dotenv import load_dotenv
import pairs

load_dotenv(override=True)

HTTPS_URL = os.getenv('HTTPS_URL')
PRIVATE_KEY = os.getenv('PRIVATE_KEY')

w3 = Web3(Web3.HTTPProvider(HTTPS_URL))
caller = "0x5cF32568494B75b45bf3c125a0614117dF47F407"

mywallet = Web3.to_checksum_address("0x5cF32568494B75b45bf3c125a0614117dF47F407")
Arb_Contract = Web3.to_checksum_address("0xa6653421CE72a56df5C58D6e1548c57e6972BEA5")
usdt = Web3.to_checksum_address("0x4988a896b1227218e4A686fdE5EabdcAbd91571f")

Arb_Contract_Abi = json.load(open('src/abi/Arb.json', 'r'))
Arb = w3.eth.contract(Arb_Contract, abi=Arb_Contract_Abi)

usdt_Abi = json.load(open('src/abi/usdt.json', 'r'))
usdt_contract = w3.eth.contract(usdt, abi=usdt_Abi)

balance = usdt_contract.functions.balanceOf(Arb_Contract).call()
nonce = w3.eth.get_transaction_count(caller)
logger.info(f'wallet usdt balance : {balance}')

targetProfit = (balance + (1 * (10 ** 5)))

while True:
    a1, a2, a3, a4 = pairs.choose()
    try:
        amtBack = Arb.functions.estimateDualDexTrade(a1, a2, a3, a4,(balance)).call()
        if amtBack > targetProfit:
            logger.success(amtBack)
        else:
            pass
    except Exception as e:
        pass