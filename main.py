from controllers import CoinExchange


if __name__ == "__main__":
    CoinExchange.measure_and_print_execution_time()
    CoinExchange.measure_and_print_execution_time(iterations=1000)
    CoinExchange.measure_and_print_execution_time(iterations=10000)
