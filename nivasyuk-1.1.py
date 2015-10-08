"""
Stock price summary:  write a program that takes three arguments:  a summary type (see below), a number of trading days (up to 251 in the 12 months represented in the sample data), and a stock ticker (AAPL, FB, GOOG, LNKD, MSFT stock price files are located in the stock_prices folder on the source data page linked from the course home page).
The script will compile a list of closing prices over the specified number of trading days (counting backwards from most recent date).
Make sure to validate all user input and respond with proper error messages / behaviors as appropriate.
Source data can be found in the data directory under the stock_prices folder.
Please use a container to gather the prices and summarize them.

Summary types to support:
a.    Max price
b.    Min price
c.    Simple average (# of days / sum of prices)
d.    Median
e.    "Centered" average
"""

import argparse

#---------------------------------------------------------------------------#

def median(numbers):
    """
    Calculates the median of the given list of numbers.
    :param numbers: list of floating point numbers
    :return: median value
    """

    length = len(numbers)
    sorted_numbers = sorted(numbers)

    if length % 2 == 1:
        index = length // 2
        result = sorted_numbers[index]
    else:
        index1 = length // 2
        index2 = length // 2 - 1
        result = (sorted_numbers[index1] + sorted_numbers[index2]) / 2

    return result

def centered(numbers):
    """
    Returns 'centered average' - median with the highest and lowest values discarded and any duplicate numbers removed.
    :param numbers: list of floating point numbers
    :return: 'centered average'
    """

    sorted_numbers = sorted(set(numbers))
    data = sorted_numbers[1:-1]
    result = median(data)

    return result

def summarize_prices(prices, summary_type):
    """
    Summarizes a list of prices according to summary_type code
    :param prices: list of floating point numbers
    :param summary_type: one of: 'max', 'min', 'average', 'median', 'centered'
    :return: summary value, floating point number
    """

    result = None

    if summary_type == 'max':
        result = max(prices)

    elif summary_type == 'min':
        result = min(prices)

    elif summary_type == 'average':
        result = sum(prices) / len(prices)

    elif summary_type == 'median':
        result = median(prices)

    elif summary_type == 'centered':
        result = centered(prices)

    return result

def read_filter_data(ticker, num_days):
    """
    Takes ticker and number of days to get the associated prices.
    :param ticker: ticker symbol of company
    :param num_days: number of days of data to read
    :return: list of closing prices for the requested number of days
    """

    filename = "../data/stock_prices/" + ticker.lower() + ".csv"

    with open(filename) as fh:
        lines = fh.readlines()

    prices = [float(line.split(',')[4]) for line in lines[1:num_days + 1]]
    return prices

def validate_input(summary_type, num_days, ticker):
    """
    Validate the inputs received by the script, throw exception if invalid.
    :param summary_type: must be either: 'max', 'min', 'average', 'median', 'centered'
    :param num_days: positive int, up to 251
    :param ticker: must be one of: AAPL, FB, GOOG, LNKD, MSFT - case insensitive
    :return: no return value
    """

    if summary_type not in {'max', 'min', 'average', 'median', 'centered'}:
        raise Exception("type '{0}' not found".format(summary_type))

    if num_days <= 0 or num_days > 251:
        raise Exception("invalid number of days: '{0}'; enter 1 - 251".format(num_days))

    if ticker.upper() not in {"AAPL", "FB", "GOOG", "LNKD", "MSFT"}:
        raise Exception("'{0}' entry invalid, enter: AAPL, FB, GOOG, LNKD, MSFT".format(ticker))


def main(summary_type, num_days, ticker):
    """
    Solve the homework problem, i.e. print a summary of last num_days of ticker's closing prices
    :param summary_type: one of: 'max', 'min', 'average', 'median', 'centered'
    :param num_days: number of days of closing prices to consider, going back from most recent date
    :param ticker: valid ticker symbol for a public company
    :return: no return value
    """

    validate_input(summary_type, num_days, ticker)
    prices = read_filter_data(ticker, num_days)
    summary = summarize_prices(prices, summary_type)
    print summary

#---------------------------------------------------------------------------#

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='homework.1.1.b')
    parser.add_argument('summary_type', type=str,
                        help="- max, min, average, median, or centered")
    parser.add_argument('num_days', type=int,
                        help="- the number of trading days (up to 251)")
    parser.add_argument('ticker', type=str,
                        help="- stock ticker (AAPL, FB, GOOG, LNKD, MSFT)")

    args = parser.parse_args()

    try:
        main(args.summary_type, args.num_days, args.ticker)

    except Exception as e:
        print "Error: ", e
        parser.print_usage()

