# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?
def fact(i,num):
 while i < num+1:
  if(num%i == 0):
   break
  i+=1
 return i
a = 6008514751431
j = 2
j = fact(j,a) 
while j < a :
 #while a%j==0:
 a = a/j
 j = fact(j,a) 
print j
