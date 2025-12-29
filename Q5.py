num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

num1 = int(num1)
num2 = int(num2)

print(f"Sum: {num1 + num2}")
print(f"Difference: {num1 - num2}")
print(f"Product: {num1 * num2}")
if num1 > num2:
    print(f"{num1} is bigger than {num2}")
elif num2 > num1:
    print(f"{num2} is bigger than {num1}")
else:
    print("Both numbers are equal")
