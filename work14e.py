# The following iterative sequence is defined for the set of positive integers:

# n  n/2 (n is even)
# n  3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13  40  20  10  5  16  8  4  2  1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.
temp = { 1: 1 }
def cal(n):
    if not temp.get(n,0):
        if n % 2: temp[n] = 1 + cal(3*n + 1)
        else: temp[n] = 1 + cal(n/2)
    return temp[n]
m = 0
n = 0
for i in xrange(1, 1000000):
	c = cal(i)
	if c > m: 
		m = c
		n = i
print n