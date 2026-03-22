# Program to generate Fibonacci series up to n terms

def fibonacci(n):
    a, b = 0, 1
    series = []
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

if __name__ == "__main__":
    n = int(input("Enter the number of terms: "))
    result = fibonacci(n)
    print("Fibonacci series:", result)