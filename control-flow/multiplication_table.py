
# Multiplication Table

number = int(input("Enter a number to see its multiplication table: "))

if number != 0:
    for multiplier in range(1, 11):
        print(f"{number} x {multiplier} = {number * multiplier}")
else:
    print("Error: Multiplication by zero is not meaningful.")

