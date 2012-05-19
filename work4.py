# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91  99.

# Find the largest palindrome made from the product of two 3-digit numbers.
from sys import exit
i = 999
l = []
while i > 99:
 j = 999
 while j > 99:
  n = i*j
  l = []
  while n>0:
   l.append(n%10)
   n=n/10
  lenth = len(l)
  m=lenth/2-1
  while m >= 0:
   if l[m]!=l[lenth-m-1]:
    break
   m-=1
  if m == -1:
   print i,"x",j,"=",l
   exit(0)
  j-=1
 i-=1