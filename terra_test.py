from terra_sdk.client.lcd import LCDClient
from terra_sdk.key.mnemonic import MnemonicKey
from terra_sdk.core.bank import MsgSend
import asyncio
from api_utilities import NFTDatabase

mk = MnemonicKey("beauty artwork person capital traffic balcony where that appear jungle error flush space fresh attract twin series elevator animal tree lobster matter quick isolate")
mk2 = MnemonicKey("flavor shield elevator oppose tip tail hundred step food citizen dial comfort civil grab jelly endless book grocery change switch become invite pupil history")
terra = LCDClient(chain_id="columbus-4", url="https://lcd.terra.dev")
print(mk.acc_address)
send = MsgSend(mk.acc_address, mk2.acc_address, terra.bank.balance(mk.acc_address))
# folder = 'trashgang-site/src/Sample NFTs'
# nft_db = NFTDatabase(folder)
# print(nft_db.get_random_nft())