from Crypto.Util.number import getPrime
import time

seenNumbers = set()
bitSize = 1024
attempts = 0

start = time.time()

while True:
    primes = getPrime(bitSize // 2)
    print(primes)
    attempts += 1

    if primes in seenNumbers:
        print(f"Repeat Found {primes}")
        break

    seenNumbers.add(primes)


end = time.time()
duration = end - start

print(f"Number of attempts: {attempts}")
print(f"Time taken: {duration}")
