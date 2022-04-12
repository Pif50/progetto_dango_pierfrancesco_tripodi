from web3 import Web3


def sendTransaction(message):
    w3 = Web3(Web3.HTTPProvider('https://ropsten.infura.io/v3/0bd7f96ab76b4ab697009051a025312f'))
    address = '0x4C61CE130C77328Ebe8f0F3DF3EFee8c8202a438'
    privateKey = '0x3cbbcd01a98ac0a978b2d9a5945e104b571ea69f172d6fd9069f6d0b755bbdda'
    nonce = w3.eth.getTransactionCount(address)
    gasPrice = w3.eth.gasPrice
    value = w3.toWei(0, "ether")
    signedTx = w3.eth.account.sign_transaction(dict(
        nonce=nonce,
        gasPrice=gasPrice,
        gas=100000,
        to="0x0000000000000000000000000000000000000000",
        value=value,
        data=message.encode('utf-8')
    ), privateKey)
    tx = w3.eth.sendRawTransaction(signedTx.rawTransaction)
    txId = w3.toHex(tx)
    return txId