from matplotlib import pyplot as plt

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales =  [91, 76, 56, 66, 52, 27]

plt.bar(range(len(drinks)), sales)

#create your ax object here
ax = plt.subplot()
ax.set_xticks([0,1,2,3,4,5])
ax.set_xticklabels(["cappuccino", "latte", "chai", "americano", "mocha", "espresso"])
plt.show()