# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?
from math import sqrt
a = []
e=2
a.append(2)
a.append(3)
i = 5
z = 4
while z < 10001:
	c=0
	if i%3!=0 and i%5!=0 and i%7!=0:
		for j in range(0,e):
			if a[j] > int(sqrt(i)):
				break
			if i%a[j] == 0:
				c+=1
				break
		
		if(c==0):
			
			a.append(i)
			e+=1
			z+=1
	i=i+2
print a.pop()