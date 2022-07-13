"""
Working with list and using a Pizza restaurant as the theme
"""

toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
price = [2, 6, 1, 3, 2, 7, 2]

# counts number of times 2 or $2 comes up
num_two_dollar_slices = price.count(2)
print(num_two_dollar_slices) # display 3 (3 times)

num_pizzas = len(toppings) # counts number of toppings available

print("We sell: " + str(num_pizzas) + " different kinds of pizza!")

# Combing toppings and price into a 2d list
pizza_and_prices = [[2,	"pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]
# sort pizza by price ascending
pizza_and_prices.sort()
print(pizza_and_prices)

# Find the cheapest pizza using first index
cheapest_pizza = pizza_and_prices[0]
 print("Cheapest Pizza: " + str(cheapest_pizza))

# Find the priciest pizza using the last index
priciest_pizza = pizza_and_prices[-1]
print("Pricisest Pizza: " + str(priciest_pizza))

# Take off last pizza option as its been 'sold'
pizza_and_prices.pop()
print(pizza_and_prices)

# Add new item to menu
pizza_and_prices.insert(4,[2.5, "peppers"])
print(pizza_and_prices)

# print out the three cheapeast items on the menu
three_cheapest = pizza_and_prices[:3]
print(three_cheapest)
