# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
def fact(r,n):
	for i in range(r,n+1):
		if n%i==0:
			return i
	return i
def power(n,p):
	s = 1
	for i in range(0,p):
		s = s*n
	return s
input = 20
cp = []
for i in range(0,input):
	cp.append(0)
for i in range(2,input+1):
	d = 2
	num = i
	cl = []
	for i in range(0,input):
		cl.append(0)
	while d <= num:
		d = fact(d,num)
		num = num/d
		
		
		cl[d] += 1

	for i in range(0,input):
		if cp[i]<cl[i]:
			cp[i]=cl[i]
s = 1  
for i in range(1,input):
	s=s*power(i,cp[i])
print s