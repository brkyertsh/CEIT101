# Part A
def leap_year(year):
	year = int(year)
	if year%4 == 0 and year%100 != 0:
		return True
	elif year%400 == 0:
		return True
	else:
		return False

# Part A, Optional Challenge 
def leap_year_oc(year):
	return True if int(year)%4 == 0 and int(year)%100 != 0 or int(year)%400 == 0 else False 

# Part B
def rotate(s,n):
	if s == "" or len(s) == 1:
		return s
	else:
		s = s[len(s)-n:] + s[0:len(s)-n]
		return s
'''
Analyzing these tests may help you 
understand what the function is doing.

s = "abc" # 2
s = s[1:] + s[0:1]
print(s)

s = "abcd" # 2
s = s[2:] + s[0:2]
print(s)

s = "abcd" # 3
s = s[1:] + s[0:1]
print(s)

Part B, optional challenge is not clear. If n is given bigger
than len(s), should the function just reverse the string or 
after reversing should it continue to do something else?
'''

# Part C
def digit_count(n):
	even_count, odd_count, zero_count = 0, 0, 0
	if n == 0: # If n=0 without a fractional part, return zero_count = 1
		return even_count, odd_count, zero_count+1
	n = int(n) # By converting into int, we get rid of the fractional part.
	if n == 0: # In case of a edge case such as n = 0.53.
		return even_count, odd_count, zero_count
	n = str(n) # To be able iterate over n.

	for i in n:
		if int(i)%2 == 0 and int(i) != 0:
			even_count += 1
		elif int(i)%2 != 0:
			odd_count += 1
		else:
			zero_count += 1

	return even_count, odd_count, zero_count

# Part D
def float_check(s):
	if s.replace('.', '', 1).isdigit() == True:
		return True
	else:
		return False
# for replace() method, https://www.w3schools.com/python/ref_string_replace.asp

# Part D, Optional Challenge
def float_check_oc(s):
	return True if s.replace('.', '', 1).isdigit() == True else False
	
