import numpy as np

np.random.seed(42)
stock_prices = np.random.randint(100, 501, size=(30, 5))

avg_prices = np.mean(stock_prices, axis=0)
print("Average stock prices:", np.round(avg_prices, 1))

max_value = np.max(stock_prices)
max_index = np.unravel_index(np.argmax(stock_prices), stock_prices.shape)
day, company = max_index
print(f"Highest price recorded: {max_value} at Day {day}, Company {company}")

min_price = np.min(stock_prices)
max_price = np.max(stock_prices)
normalized_prices = (stock_prices - min_price) / (max_price - min_price)

print("\nNormalized prices:")
for row in normalized_prices:
    formatted_row = ["{:0.2f}".format(val) for val in row]
    print(" ".join(formatted_row))

print("\nRisky Investment Days:")
for day_idx, prices in enumerate(stock_prices):
    risky_prices = prices[prices < 200].tolist()  
    if risky_prices:
        print(f"Day {day_idx}: {risky_prices}")