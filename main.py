from web3 import Web3
from colorama import init, Fore, Style
import sys
import time

init(autoreset=True)

class HumanityProtocolBot:
    def __init__(self):
        self.display_header()
        self.web3 = self.setup_blockchain_connection('https://rpc.testnet.humanity.org')
        self.contract = self.setup_contract()

    @staticmethod
    def display_header():
        """"""
        header_text = """
               ╔═╗╔═╦╗─╔╦═══╦═══╦═══╦═══╗
               ╚╗╚╝╔╣║─║║╔══╣╔═╗║╔═╗║╔═╗║
               ─╚╗╔╝║║─║║╚══╣║─╚╣║─║║║─║║
               ─╔╝╚╗║║─║║╔══╣║╔═╣╚═╝║║─║║
               ╔╝╔╗╚╣╚═╝║╚══╣╚╩═║╔═╗║╚═╝║
               ╚═╝╚═╩═══╩═══╩═══╩╝─╚╩═══╝
               我的gihub：github.com/Gzgod
               我的推特：推特雪糕战神@Hy78516012   
        """
        print(Fore.CYAN + Style.BRIGHT + header_text + "\n")

    @staticmethod
    def setup_blockchain_connection(rpc_url):
        """设置并验证区块链连接"""
        web3 = Web3(Web3.HTTPProvider(rpc_url))
        if web3.is_connected():
            print(Fore.GREEN + "已连接到掌纹协议")
        else:
            print(Fore.RED + "连接失败。")
            sys.exit(1)
        return web3

    @staticmethod
    def load_private_keys(file_path):
        """从指定文件加载私钥"""
        with open(file_path, 'r') as file:
            return [line.strip() for line in file if line.strip()]

    def setup_contract(self):
        """使用 ABI 和地址初始化合约对象"""
        contract_address = '0xa18f6FCB2Fd4884436d10610E69DB7BFa1bFe8C7'
        contract_abi = [
            # ... 这里包含你的ABI，实际代码中应使用完整的ABI ...
        ]
        return self.web3.eth.contract(address=Web3.to_checksum_address(contract_address), abi=contract_abi)

    def claim_rewards(self, private_key):
        """为给定的私钥处理奖励领取"""
        account = self.web3.eth.account.from_key(private_key)
        sender_address = account.address
        genesis_claimed = self.contract.functions.userGenesisClaimStatus(sender_address).call()
        current_epoch = self.contract.functions.currentEpoch().call()
        buffer_amount, claim_status = self.contract.functions.userClaimStatus(sender_address, current_epoch).call()

        if genesis_claimed and not claim_status:
            print(Fore.GREEN + f"正在为地址领取奖励: {sender_address} (已领取初始奖励)。")
            self.process_claim(sender_address, private_key)
        elif not genesis_claimed:
            print(Fore.GREEN + f"正在为地址领取奖励: {sender_address} (未领取初始奖励)。")
            self.process_claim(sender_address, private_key)
        else:
            print(Fore.YELLOW + f"地址 {sender_address} 在第 {current_epoch} 周期中已领取奖励。跳过。")

    def process_claim(self, sender_address, private_key):
        """发送交易以领取奖励"""
        try:
            transaction = self.contract.functions.claimReward().build_transaction({
                'chainId': self.web3.eth.chain_id,
                'from': sender_address,
                'gas': self.contract.functions.claimReward().estimate_gas({'from': sender_address}),
                'gasPrice': self.web3.eth.gas_price,
                'nonce': self.web3.eth.get_transaction_count(sender_address)
            })
            signed_txn = self.web3.eth.account.sign_transaction(transaction, private_key=private_key)
            tx_hash = self.web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            self.web3.eth.wait_for_transaction_receipt(tx_hash)
            print(Fore.GREEN + f"地址 {sender_address} 的交易成功，交易哈希: {self.web3.to_hex(tx_hash)}")
        except Exception as e:
            print(Fore.RED + f"处理领取时出错，地址 {sender_address}: {str(e)}")

    @staticmethod
    def handle_error(e, address):
        """处理并记录奖励领取过程中的任何错误"""
        error_message = str(e)
        if "Rewards: user not registered" in error_message:
            print(Fore.RED + f"错误：用户 {address} 未注册。")
        else:
            print(Fore.RED + f"领取奖励时出错，地址 {address}: {error_message}")

    def run(self):
        """运行机器人的主循环"""
        while True:
            private_keys = self.load_private_keys('private_keys.txt')
            for private_key in private_keys:
                try:
                    self.claim_rewards(private_key)
                except Exception as e:
                    self.handle_error(e, self.web3.eth.account.from_key(private_key).address)
            
            print(Fore.CYAN + "等待6小时后进行下一次运行...")
            time.sleep(6 * 60 * 60)  # 测试目的，你可能想减少这个时间

if __name__ == "__main__":
    bot = HumanityProtocolBot()
    bot.run()
