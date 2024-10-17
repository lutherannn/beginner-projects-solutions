def checkPrime(n):
    n = int(n)
    if n > 1:
        for i in range(2, (n//2) + 1):
            if n % i == 0:
                return False
        return True
    return False

for x in range(1, 1001):
    x = str(x)
    if len(x) > 1:
        if "1" not in x:
            if "7" not in x:
                if checkPrime(x):
                    if sum([int(d) for d in x]) <= 10:
                        if sum([int(d) for d in x[0:2]]) % 2 != 0:
                            if int(x[::-1][1]) > 1:
                                if int(x[::-1][1]) % 2 == 0:
                                    if len(x) == int(x[-1]):
                                        print(x)