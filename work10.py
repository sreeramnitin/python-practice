# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.
from math import sqrt
a = []
e=2
a.append(2)
a.append(3)
i = 5
z = 5
while z <= 100000:
	c=0
	if i%3!=0 and i%5!=0 and i%7:
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
s = 0
for i in range(0,len(a)):
	 s += a[i]
print s+5+7