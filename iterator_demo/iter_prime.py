class PrimeNumbers:
    def __init__(self, start=1, end=100):
        self.end = end
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        while self.current <= self.end:
            if self.is_prime(self.current):
                prime = self.current
                self.current += 1
                return prime
            self.current += 1
        raise StopIteration

    def is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

# Example usage:
primes = PrimeNumbers(1, 100)
for prime in primes:
    print(prime)
