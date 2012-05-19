# Starting in the top left corner of a 22 grid, there are 6 routes (without backtracking) to the bottom right corner.


# How many routes are there through a 2020 grid?
def fact(n):
    f = 1
    for x in xrange(1, n+1): f = f * x
    return f
#a=20
a=int(raw_input("enter size of grid"));
print fact(2*a) / fact(a) / fact(a)