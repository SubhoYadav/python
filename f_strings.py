name = "Subho"
coins = 10

print(name + " has " + str(coins) + " left.")

print("\n%s has %s coins left" % (name, coins))

print("\n{} has {} coins left".format(name, coins))

print("\n{0} has {1} coins left".format(name, coins))

print("\n{name} has {coins} coins left".format(name = name, coins = coins))

player = {
    "name": "Subho",
    "coins": 10
}

print("\n{name} has {coins} coins left".format(**player))


print(f"{name} has {coins} coins left.")

for num in range(1, 11):
    # optional formatting fixes the digits after decimal point to 3
    print(f"4.25 times {num:.3f} equals {num * 4.25}")

for num in range(1, 11):
    # optional formatting fixes the digits after decimal point to 2 and adding a % sign also
    print(f"4.25 times {num:.2%} equals {num / 4.25:.2%}")