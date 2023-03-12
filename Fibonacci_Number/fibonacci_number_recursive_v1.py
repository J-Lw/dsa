#Recursive fibonacci algorithm

_MAX_N = 100
_MIN_N = 1

def derive_fibonacci_number(n: int) -> int:
   if n > _MAX_N or n < _MIN_N:
        return -1
   if n <= 2:
        return 1
   if n > 2:
      return derive_fibonacci_number(n-1) + derive_fibonacci_number(n-2)