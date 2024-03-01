"""Bureau de Change

This Python program simulates a currency exchange program named
"Bureau de Change".

Author: Charis Adu
Version: 1.0
"""
import requests
import pandas as pd
import csv


def main():
    """
    Main function that orchestrates the currency exchange process.
    """

    ex, cu = get_transaction()
    download_rates("exchange.csv")
    ex_rate = get_exchange_rate("exchange.csv", ex, cu)
    amt = get_amount()
    money = convert(ex, ex_rate, amt)
    if ex == 'to naira':
        cu = 'ngn'
    print(f"Here's your money: {money: .2f}{cu.upper()}. Please come again")


def get_transaction():
    """
    Prompts the user for the type of exchange and chosen currency.
    Returns the exchange type ("to naira" or "to other") and chosen
    currency code ("usd", "gbp", or "eur").
    """

    print(
        "Welcome to Bureau de Change. \n"
        "What exchange would you like to carry out?"
    )
    exchange = ''
    while exchange not in ["to naira", "to other"]:
        exchange = input(
            "Type 'to naira' to exchange other currencies for "
            "naira or 'to other' to exchange naira for other "
            "currencies: "
        ).strip().lower()

    if exchange == "to naira":
        print("What currency would you like to convert to naira?")
    else:
        print("What currency would you like to convert your naira "
              "to?")

    tr_msg = (
        "Type 'usd' for US dollars, 'gbp' for Pounds "
        "sterling, or 'eur' for Euros: "
    )
    currency = ''
    while currency not in ["usd", "gbp", "eur"]:
        currency = input(tr_msg).strip().lower()

    return exchange, currency


def download_rates(file_name):
    """
    Function to download current exchange rates from the CBN website and
    save them to a CSV file.

    Args:
        file_name (str): Name of the file to download the rates to.
    """

    print("Getting current rates...")
    res = requests.get(
        "https://www.cbn.gov.ng/Functions/export.asp?"
        "tablename=exchange"
    )
    with open(file_name, "wb") as f:
        f.write(res.content)


def get_exchange_rate(file_name, exchange, currency):
    """
    Reads the exchange rate file, finds the relevant rate based on
    user choices, and prints it to the console.

    Args:
        file_name (str): Name of the file containing exchange rates.
        exchange (str): Type of exchange ("to naira" or "to other").
        currency (str): Chosen currency code ("usd", "gbp", or "eur").

    Returns:
        float: The exchange rate for the chosen currency.
    """

    with open(file_name, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        cols = next(reader)
        data_rows = []
        for row in reader:
            data_rows.append(row[:-1])

    df = pd.DataFrame(data_rows, columns=cols)
    df = df.head(10)
    df.set_index('Currency', inplace=True)

    match currency:
        case 'usd':
            currency = 'US DOLLAR'
        case 'gbp':
            currency = 'POUNDS STERLING'
        case 'eur':
            currency = 'EURO'

    if exchange == 'to naira':
        rate = 'Buying Rate'
        exchange_rate = float(df.loc[currency][rate])
        print(
            f"We buy {currency} at {exchange_rate} Naira per {currency}"
        )
    else:
        rate = 'Selling Rate'
        exchange_rate = float(df.loc[currency][rate])
        print(
            f"We sell {currency} at {exchange_rate} Naira per {currency}"
        )

    return exchange_rate


def get_amount():
    """
    Prompts the user for the amount to be exchanged. Loops until a
    valid number is entered.

    Returns:
        float: The amount entered by the user.
    """
    msg = "How much would you like to exchange? "
    while True:
        try:
            amount = float(input(msg).strip())
            return amount
        except ValueError:
            print("Please input digits only")
            continue


def convert(exchange, rate, amount):
    """
    Performs the currency conversion based on the exchange type,
    rate, and amount.

    Args:
        exchange (str): Type of exchange ("to naira" or "to other").
        rate (float): The exchange rate for the chosen currency.
        amount (float): The amount to be converted.

    Returns:
        float: The converted amount.
    """
    if exchange == 'to naira':
        return amount * rate
    else:
        return amount / rate


if __name__ == "__main__":
    main()
