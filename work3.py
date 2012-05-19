# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?
def fact(r,num):
 for i in range(r,num+1):
  if(num%i == 0):
   break
 return i
a = 60
j = 2
j = fact(j,a) 
while j < a :
 a = a/j
 while a%j==0:
	a=a/j
 print j,a
 j = fact(j,a) 
print j