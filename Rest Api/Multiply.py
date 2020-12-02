def multiply(a: int, b: int) -> str:
    if isinstance(a, int) == False or isinstance(b, int) == False:
        print("not int value")
        raise
    if a < 0 or b < 0:
        print("negative number")
        raise
    c=0
    for i in range(b):
        c += a
    return c