#print(10 // 3)
# / Returns exact division, // returns a whole number rounded down
# print(10 % 3) Modulous operator
# Returns remainder of the division
# print(10 ** 3) Exponent operator; 10 to the power of 3


# x = 10 

# x = x + 3 is the same as x += 3

# x = 10 + 3 * 2 = 16 (Operator precedence. Multiplication + division gets precedence)

# x = (10 + 3) * 2 = 26



# price = 25
# print(price > 10 and price < 30)

# price = 5
# print(price > 10 or price < 30)

# price = 5
# print(not price > 10)

# and (both)
# or (at least one)
# not (opposite)

tempurature = 10

if tempurature > 30 : 
    print("It's a hot day!")
    print("Drink some water to stay hydrated!")
elif tempurature > 20: # (20-30)
    print("It's a nice day.")
elif tempurature > 10: #(10-20)
    print("It's a bit chilly.")
else:
    print("It's FREEZING outside. It would be best to stay in today.")

print("Done")
