# A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
a = 1
for a in range(1,333):
	b = a + 1
	c = 1000 - a - b
	while b < c:
		if a * a + b * b == c * c :
			print a,b,c
		b += 1
		c -= 1