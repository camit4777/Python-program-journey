# HackerRank Problem: Python If-Else

if __name__ == "__main__":
n = int(input().strip())  # Read integer input

    if n % 2 != 0:  # Odd number
        print("Weird")
    elif n % 2 == 0 and 2 <= n <= 5:
        print("Not Weird")
    elif n % 2 == 0 and 6 <= n <= 20:
        print("Weird")
    elif n % 2 == 0 and n > 20:
        print("Not Weird")