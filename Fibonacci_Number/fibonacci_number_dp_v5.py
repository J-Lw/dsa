#DP fibonacci algorithm using two variables

_MAX_N = 100
_MIN_N = 1

def derive_fibonacci_number(n: int) -> int:
    n_1 = 1
    n_2 = 1
    if n > _MAX_N or n < _MIN_N:
        return -1
    if n < 2:
        return n_1
    for _ in range(2, n+1):  
        n_0 = n_1 + n_2
        n_2 = n_1
        n_1 = n_0
    return n_1