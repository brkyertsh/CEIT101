# Throughout the code, there may be some comments to help you. 
# They explain or direct you to a link.
# Scroll to bottom to see the explanations.

with open("scores.txt") as f: # 0 with open()
	lines = [line.split() for line in f]

scores = [[int(line[i+2]) for i in range(4)] for line in lines] # 1 w/out list comp.
means = [sum(scores[count])/4 for count, student in enumerate(scores)] # 2 """
exam_means = [] # 3 w/ list comp.
for exam in range(4):
	mean = 0
	for student in range(5):
		mean += scores[student][exam]/5
	exam_means.append(mean)

data = []
for i in range(5):
	tuplex = ()
	for j in range(2):
		tuplex += (lines[i][j],) # 4 on tuples
	tuplex += (scores[i],)
	tuplex += (means[i],)
	data.append(tuplex)

data.sort()
print("{:23s}{:6s}{:6s}{:6s}{:8s}{:10s}".format("Name", "Exam1", 
	"Exam2", "Exam3", "Exam4", "Mean"))

for student in data:
	name = student[0] + " " + student[1]
	print("{:20s}{:6d}{:6d}{:6d}{:6d}{:10.2f}".format(name, student[2][0], 
		student[2][1], student[2][2], student[2][3], student[3]))

print("{:21s}{:6.1f}{:6.1f}{:6.1f}{:6.1f}".format("Exam Mean ",exam_means[0], exam_means[1], exam_means[2], exam_means[3]))

   

'''
0
Using the with statement we don't have to use close(). For further info:
https://cmdlinetips.com/2016/01/opening-a-file-in-python-using-with-statement/

1
scores = []
for line in lines:
	scores_of_line = []
	for i in range(4):
		scores_of_line.append(int(line[i+2]))
	scores.append(scores_of_line)
2
means = []
for count, student in enumerate(scores):
	means.append(sum(scores[count])/4)
3
exam_means = [sum([scores[student][exam] for student in range(5)])/5 for exam in range(4)]

4
tuples are immutable so instead of sth like append() we create 
a new tuple by adding the old one and "the modification" together 
using +=. The modification part should be in parentheses (can only
add tuple to tuple) with a comma like this (mod, ). W/out the comma
the thing we are trying to add does not interpreted as a tuple.
'''

