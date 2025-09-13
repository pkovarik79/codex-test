"""Calculator module providing factorial function."""

def factorial(n: int) -> int:
    """Return the factorial of a non-negative integer n.

    Args:
        n: A non-negative integer whose factorial is to be computed.

    Returns:
        The factorial of n.

    Raises:
        ValueError: If n is negative.
        TypeError: If n is not an integer.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be >= 0")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
