def mult(base, num):
    if num == 1:
        """set base case which will stop making recursive calls and finish function"""
        return base

    return base + mult(base, num-1)

print(mult(9, 5))