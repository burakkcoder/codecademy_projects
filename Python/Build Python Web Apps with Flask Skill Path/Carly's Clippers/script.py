hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0
for x in prices:
    total_price += x

average_price = total_price / len(prices)
print(f"Average Haircut Price: {average_price}")

new_prices = [x - 5 for x in prices]
print(new_prices)

total_revenue = 0
for x in range(len(hairstyles)):
    total_revenue += new_prices[x] * last_week[x]
print(f"Total Revenue: {total_revenue}")

average_daily_revenue = total_revenue / 7

cuts_under_30 = [hairstyles[x] for x in range(len(new_prices) - 1) if new_prices[x] < 30]
print(cuts_under_30)