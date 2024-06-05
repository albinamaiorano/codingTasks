def fibonacci(n):
    """
    Generates the Fibonacci series up to the nth term.

    Parameters:
    n (int): The number of terms in the Fibonacci series to generate.

    Returns:
    list: The Fibonacci series up to the nth term.
    """
    # Initialize the Fibonacci series with the first two terms
    fib_series = [0, 1]

    # Check if n is less than or equal to 1
    if n <= 1:
        # If so, return the first n + 1 terms of the Fibonacci series
        return fib_series[:n + 1]
    else:
        # If n is greater than 1, generate the Fibonacci series up to the nth term
        for i in range(2, n):
            # Calculate the next term in the Fibonacci series
            next_term = fib_series[-1] + fib_series[-2]
            # Append the next term to the Fibonacci series
            fib_series.append(next_term)
        
        # Return the generated Fibonacci series
        return fib_series

if __name__ == "__main__":
    # Define the number of terms in the Fibonacci series
    n = 10
    # Print a message indicating the number of terms
    print(f"Fibonacci series up to {n} terms:")
    # Generate and print the Fibonacci series up to the nth term
    for i in range(n):
        print(fibonacci(i), end=" ")
