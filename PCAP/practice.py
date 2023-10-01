'''
power = 1
for expo in range(16):
    print("2 to the power of", expo, "is", power)
    power *= 2

# break - example

print("The break instruction:")
for i in range(1, 6):
    if i == 3:
        break
    print("Inside the loop.", i)
print("Outside the loop.")


# continue - example

print("\nThe continue instruction:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Inside the loop.", i)
print("Outside the loop.")
'''
n = int (input ("Choose number: "))
print ( n >= 100)
