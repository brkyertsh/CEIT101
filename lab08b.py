with open("data1.txt", "r") as f:
	data1 = [line.split() for line in f]
	data1.remove(data1[0])
	print(data1)

with open("data2.txt", "r") as s:
	data2 = [line.split() for line in s]
	data2.remove(data2[0])
	print(data2)

data_dict = {}

def construct_dict(my_dict):
	for i in range(4):
		my_dict[ data1[i][0] ] = int(data1[i][1])

	for i in range(4):
		if data2[i][0] in my_dict: # Check if a student was already added from data1
			for j in range(4):
				if data1[j][0] == data2[i][0]: # Find the index of that student to find his score 
					my_dict[ data2[i][0] ] = int(data1[j][1]) + int(data2[i][1])
		else:
			my_dict[ data2[i][0] ] = int(data2[i][1]) # Else directly add him

	return my_dict

data_dict = construct_dict(data_dict)

def print_dict(my_dict):
	print("{:18s} {:10s}".format("Name", "Score"))
	for k,v in my_dict.items():
		print("{:10s} {:10d}".format(k, v))

print_dict(data_dict)