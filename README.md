# BUREAU DE CHANGE
#### Video Demo:  <https://youtu.be/8_zsFFGzfdw>
#### Description:
This project simulates a currency exchange program named "Bureau de Change" using Python. It allows users to experience exchanging foreign currencies to Naira or vice versa, similar to a real-world currency exchange office. 

The project consists of several key files:

- **main.py:** This is the core script that orchestrates the entire currency exchange process. It calls various functions to handle user interaction, retrieve exchange rates, perform calculations, and display the final converted amount. Functions found in this file include:
  - **download_rates.py:** This function downloads the latest exchange rates from the Central Bank of Nigeria (CBN) website and saves them to a CSV file.
  - **get_transaction.py:** This function gathers user input regarding the type of exchange (to Naira or to other currencies) and the chosen currency (USD, GBP, or EUR).
  - **get_exchange_rate.py:** This function reads the downloaded exchange rate data (from "exchange.csv") and retrieves the specific rate based on the user's chosen currency and exchange type. It then displays the retrieved rate to the user.
  - **get_amount.py:** This function prompts the user to enter the amount of money they want to exchange and ensures they enter a valid numerical value.
  - **convert.py:** This function performs the actual currency conversion calculation based on the exchange type, chosen rate, and entered amount. It returns the converted amount to the main program.

**Functionality:**

When you run the program, it welcomes you to "Bureau de Change" and asks you to choose the type of exchange you want to perform. You can either exchange other currencies for Naira or exchange Naira for other currencies. After selecting the exchange type, you'll be prompted to choose the specific currency you want to exchange (USD, GBP, or EUR).

The program then prompts you to enter the amount you want to exchange. Once you enter a valid amount, the program (if download_rates.py is uncommented) retrieves the latest exchange rate from the CBN website or uses the data from "exchange.csv" (if downloaded previously). Based on your chosen exchange type and currency, it displays the relevant buying or selling rate. Finally, the program calculates the converted amount and displays it to you, informing you of the amount you will receive in your desired currency.

**Beyond the code:**

This project demonstrates the practical application of Python for simulating real-world scenarios. It showcases functionalities like user interaction, data retrieval, calculations, and output formatting. You can further enhance this project by:

- Expanding the program to support additional currencies beyond USD, GBP, and EUR.
- Creating a more user-friendly interface using graphical elements for a visually appealing experience.
