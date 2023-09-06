#factorial of a number using recursion
def fact(m):
  if m <= 1:
    return 1
  else:
    return m * fact(m - 1)


n = int(input("enter the value of n:"))
print("the factorial of", n, "is", fact(n))
