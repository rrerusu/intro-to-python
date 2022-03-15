# Ideas behind sequence slicing

primes = [2, 3, 5, 7, 11, 13, 17, 19]
print("primes[2:6] = ", end="")
print(primes[2:6])

print("primes[:6] = ", end="")
print(primes[:6])

print("primes[0:6] = ", end="")
print(primes[0:6])

print("primes[6:] = ", end="")
print(primes[6:])

print("primes[:] = ", end="")
print(primes[:])

print("primes[::2] = ", end="")
print(primes[::2])

print("primes[::-1] = ", end="")
print(primes[::-1])

print("primes[-1:-9:-1] = ", end="")
print(primes[-1:-9:-1])

primes[0:3] = ["two", "three", "five"]
print("replacing primes[0:3] = ", end="")
print(primes)

primes[0:3] = []
print("replacing primes[0:3] = ", end="")
print(primes)

primes = [2, 3, 5, 7, 11, 13, 17, 19]

primes[::2] = [100, 100, 100, 100]
print("replacing primes[::2] = ", end="")
print(primes)

primes[:] = []
print("replacing primes[:] = ", end="")
print(primes)