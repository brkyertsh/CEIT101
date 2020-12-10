import math

threshold = float(input("Enter a error threshold (maybe try 0.053?): "))
denominator = 1
sign = 4 # Determine the sign.
term = 1 # Assigning an arbitrary number to compare & loop through at least once.
sum = 0 # Not initiating this may result in TypeErrors as interpreter may assume it as the built-in-function sum().
count = 0

while term > threshold:
	count += 1
	sum += sign/denominator
	term = 1/denominator
	denominator += 2
	sign *= -1

print("Number of iterations is:", count, "& the last term is: 1/{}".format(denominator-2))
print("The approximation of pi is:", sum)
print("Compare this to the computer's estimation:", math.pi)

# if you give a value between nth & (n+1)th term, you will get the sum of n terms.