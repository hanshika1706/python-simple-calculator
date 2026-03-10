n = int(input("How many numbers do you want to perform the calculation on? "))

numbers = []
i = 0

while i < n:
    num = float(input("Enter number: "))
    numbers.append(num)
    i += 1

print("Choose operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter choice (1/2/3/4): ")

result = numbers[0]

i = 1
while i < len(numbers):
    if choice == '1':
        result = result + numbers[i]
    elif choice == '2':
        result = result - numbers[i]
    elif choice == '3':
        result = result * numbers[i]
    elif choice == '4':
        if numbers[i] != 0:
            result = result / numbers[i]
        else:
            print("Division by zero not allowed")
            break
    i += 1

print("Result:", result)
