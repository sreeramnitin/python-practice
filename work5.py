# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
from sys import exit
i = 2
while True:
	c=0
	for j in range(1,21):
		if i%j==0:
			c+=1
			#print c
	if c==20:
		print i
		exit(0)
	i+=1