file = open('data.txt', "r")

min_h = 3
max_h = 0
total_h = 0

min_w = 200
max_w = 0
total_w = 0

bmi = 0
max_bmi = 0
min_bmi = 200
total_bmi = 0
bmi_list = []

file.readline() # Skip the headers. readline() reads the next line each time it's called.
for i in range(8):
	hw = file.readline()[12:29].split() # Read from the first index of height to the last index of weight, then split the two values into a list.
	height = float(hw[0]) # First item of hw is height hence height = hw[0].
	total_h += height
	if min_h > height:
		min_h = height
	if max_h < height:
		max_h = height

	weight = float(hw[1]) # Second item of hw is weight hence weight = hw[1].
	total_w += weight
	if min_w > weight:
		min_w = weight
	if max_w < weight:
		max_w = weight

	bmi = weight/height**2
	bmi_list.append(bmi)
	if min_bmi > bmi:
		min_bmi = bmi
	if max_bmi < bmi:
		max_bmi = bmi
	total_bmi += bmi

average_h = total_h/8	
average_w = total_w/8
average_b = total_bmi/8

file = open('data.txt', "r") 
content = file.read().splitlines() 

new_data = open("data.txt", "w")
new_data.write(content[0] + "BMI" + "\n") 
for i in range(8): 
	new_data.write(content[i+1] + "{:>8.2f}".format(bmi_list[i]) + "\n")
	
new_data.write("\nAverage {:>9.2f} {:>13.2f} {:>12.2f}".format(average_h, average_w, average_b))
new_data.write("\nMax {:>13.2f} {:>13.2f} {:>12.2f}".format(max_h, max_w, max_bmi))
new_data.write("\nMin {:>13.2f} {:>13.2f} {:>12.2f}".format(min_h, min_w, min_bmi))

new_data.close()

