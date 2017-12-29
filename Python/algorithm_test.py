### Fbonacci Numbers
def Fibonacci(n):
	result = [0,1]

	for i in range(2,n+1):
		result.append(result[i-1]+result[i-2])
	print (result)
	return result[-1]

print (Fibonacci(10)) #10번째 값

### Anagram
def isAnagram(s1,s2):
    a = ''.join(sorted(s1.lower())).strip()
    b = ''.join(sorted(s2.lower())).strip()

    if a==b:
        return True
    else: 
        return False

print (isAnagram("Listen","slient")) # True
print (isAnagram("listen","slienk")) # False
print (isAnagram("apple","eppal")) # True
print (isAnagram("apple","epzkz")) # False#


### Fcactorial
import math
print (math.factorial(10))