# Function to print Fibonacci series up to n terms
def fibonacci(n):
    a, b = 0, 1
    print("Fibonacci Series:")
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

# Input from user
n = int(input("Enter the number of terms: "))

# Call the function
fibonacci(n)

