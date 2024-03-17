import timeit
import random
from functools import lru_cache


class CoinExchange:
    coins = [50, 25, 10, 5, 2, 1]
    change_cache = {}

    def find_coins_greedy(change):
        change_coins = {}
        rest = change
        for coin in CoinExchange.coins:
            coin_num = rest // coin
            if coin_num:
                change_coins[coin] = coin_num
                rest %= coin
            if rest == 0:
                break
        return change_coins

    @staticmethod
    def find_min_coins(change):
        if change not in CoinExchange.change_cache:
            CoinExchange.change_cache[change] = CoinExchange.find_coins_greedy(change)
        return CoinExchange.change_cache[change]

    @staticmethod
    @lru_cache
    def find_min_coins_lru(change):
        return CoinExchange.find_coins_greedy(change)

    @staticmethod
    def measure_exe_time(functions, iterations=100):
        execution_time = {function_name: 0 for function_name in functions.keys()}
        for _ in range(iterations):
            change = random.randint(1, 200)
            for function_name, func in functions.items():
                execution_time[function_name] += timeit.timeit(
                    lambda: func(change), number=1
                )
        return {func_name: t * 1000 for func_name, t in execution_time.items()}

    functions = {
        "Greedy": find_coins_greedy,
        "Min": find_min_coins,
        "Min with LRU": find_min_coins_lru,
    }

    @staticmethod
    def measure_and_print_execution_time(functions=functions, iterations=100):
        execution_time_before_caching = CoinExchange.measure_exe_time(functions)
        print(
            "\nExecution time before caching results for "
            + str(iterations)
            + " iterations"
            + " :"
        )
        for func_name, time_ms in execution_time_before_caching.items():
            print(f"\t{func_name:<15}: {time_ms:.2f} ms")

        execution_time_after_caching = CoinExchange.measure_exe_time(
            functions, iterations=iterations
        )
        print(
            "\nExecution time after caching results for "
            + str(iterations)
            + " iterations"
            + " :"
        )
        for func_name, time_ms in execution_time_after_caching.items():
            print(f"\t{func_name:<15}: {time_ms:.2f} ms")
