def sum_of_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

if __name__ == "__main__":
    n = 10  # Example input
    print(sum_of_numbers(n))
