
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGLE": 150,
    "AMZN": 170,
    "MSFT": 220
}

portfolio = {}
total_value = 0

print("=" * 45)
print("      STOCK PORTFOLIO TRACKER")
print("=" * 45)

num = int(input("Enter number of different stocks: "))

for i in range(num):
    stock = input("\nEnter Stock Name: ").upper()
    quantity = int(input("Enter Quantity: "))

    if stock in stock_prices:
        portfolio[stock] = quantity
    else:
        print("Stock not available.")

print("\nPortfolio Summary")
print("-" * 40)

for stock, quantity in portfolio.items():
    value = stock_prices[stock] * quantity
    total_value += value

    print(f"{stock}")
    print(f"Price     : ${stock_prices[stock]}")
    print(f"Quantity  : {quantity}")
    print(f"Value     : ${value}")
    print("-" * 40)

print("Total Investment Value = $", total_value)

choice = input("\nDo you want to save this report? (yes/no): ").lower()

if choice == "yes":

    with open("portfolio.txt", "w") as file:
        file.write("STOCK PORTFOLIO REPORT\n")
        file.write("=" * 40 + "\n")

        for stock, quantity in portfolio.items():
            value = stock_prices[stock] * quantity

            file.write(f"\nStock: {stock}\n")
            file.write(f"Price: ${stock_prices[stock]}\n")
            file.write(f"Quantity: {quantity}\n")
            file.write(f"Value: ${value}\n")

        file.write("\n")
        file.write(f"Total Investment Value = ${total_value}")

    print("Portfolio saved successfully as portfolio.txt")

else:
    print("Report not saved.")