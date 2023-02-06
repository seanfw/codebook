def fib(x):
    cache = {}
    def fib_inner(x):
        nonlocal cache
        if x in cache:
            return cache[x]
        if x == 0:
            return 0
        elif x == 1:
            return 1
        else:
            val = fib_inner(x - 1) + fib_inner(x - 2)
            cache[x] = val
            return val
    return fib_inner(x)

# The __name__ == '__main__' statement ensures
# that the following is only run if the file is
# run directly
if __name__ == '__main__':
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(6) == 8
    assert fib(40) == 102334155
    print("Tests passed")