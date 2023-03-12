def gcd(a, b):
    """Returns the greatest common divisor of two integers using the Euclidean algorithm."""
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    """Returns the least common multiple of two integers using the Euclidean algorithm."""
    return abs(a * b) // gcd(a, b)
