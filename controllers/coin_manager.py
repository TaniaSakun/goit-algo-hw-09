class CoinManager:
    def __init__(self, denominations):
        self.denominations = sorted(denominations, reverse=True)

    def find_coins_greedy(self, change):
        change_coins = {}
        rest = change
        for coin in self.denominations:
            coin_num = rest // coin
            if coin_num:
                change_coins[coin] = coin_num
                rest %= coin
            if rest == 0:
                break
        return change_coins
