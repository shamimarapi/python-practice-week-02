# exp1"""
"""
customer = "noor foods"
customer.upper()
print(customer)

customer = customer.upper()
print(customer)
"""

# Practice: strings can't change
"""
coat = "987o"
coat = coat.replace("o", "0")
print(coat)
"""
# Example 2: lists can change
"""
prices = [850, 1200, 400]
prices.append(3100)
prices[0] = 900
print(prices)
"""

"""
cart = ["rice", "oil"]
cart.append("sugar")
# print(cart)
cart[1] = "ghee"
# print(cart)
cart.remove("rice")
#print(cart)
"""

prices = [850, 1200, 400]
for price in prices:
    price = price * 1.1
print(prices)

prices = [850, 1200, 400]
for s in range(len(prices)):
    prices[s] = round(prices[s] * 1.1)
print(prices)
