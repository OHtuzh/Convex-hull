import math

def create_line(point1, point2):
	dx = point2[0] - point1[0]
	dy = point2[1] - point1[1]
	m = dy/dx
	b = point2[1] - m * point2[0]
	if point1[0] > point2[0]:
		return [m, b, [point2[0], point1[0]]]
	else:
		return [m, b, [point1[0], point2[0]]]

def highest_point(arr):
	k = 0
	high = arr[0][1]
	for i in range(1, len(arr)):
		if arr[i][1] > high:
			high = arr[i][1]
			k = i
	return arr[k]

def lowest_point(arr):
	k = 0
	low = arr[0][1]
	for i in range(1, len(arr)):
		if arr[i][1] < low:
			low = arr[i][1]
			k = i
	return arr[k]

def distance(point1, point2):
	return math.sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)

def nearest_points(arr, point):
	if distance(arr[0], point) < distance(arr[1], point):
		l0 = distance(arr[0], point)
		l1 = distance(arr[1], point)
	else:
		l0 = distance(arr[1], point)
		l1 = distance(arr[0], point)

	marks = [arr[0], arr[1]]

	for i in range(2, len(arr)):
		if distance(arr[i], point) < l0:
			l0 = distance(arr[i], point)
			marks[0] = arr[i]
		elif distance(arr[i], point) < l1:
			l1 = distance(arr[i], point)
			marks[1] = arr[i]
	return marks

def deleting_points_above_main_line(arr, k, c, range_of_xes):
	i = 0
	while i < len(arr):
		if range_of_xes[0] <= arr[i][0] and arr[i][0] <= range_of_xes[1] and k*arr[i][0] + c >= arr[i][1]:
			arr.pop(i)
		else:
			i += 1

def deleting_points_under_main_line(arr, k, c, range_of_xes):
	i = 0
	while i < len(arr):
		if range_of_xes[0] <= arr[i][0] and arr[i][0] <= range_of_xes[1] and k*arr[i][0] + c <= arr[i][1]:
			arr.pop(i)
		else:
			i += 1


fname = input('Enter filename - ')
fhand = open(fname)
coordinates = []
t = tuple()

for line in fhand:
	line = line.split()
	t = (float(line[0]), float(line[1]))
	coordinates.append(t)

coordinates.sort()


lowest_x = coordinates[0]
highest_x = coordinates[len(coordinates) - 1]
main_line = create_line(lowest_x, highest_x)

coordinates.pop(0)
coordinates.pop(len(coordinates) - 1)

above_main_line = list()
under_main_line = list()

apexes_above_main_line = [lowest_x, highest_x]
apexes_under_main_line = [lowest_x, highest_x]

for i in range(len(coordinates)):
	if coordinates[i][1] > main_line[0]*coordinates[i][0] + main_line[1]:
		above_main_line.append(coordinates[i])
	else:
		under_main_line.append(coordinates[i])

if len(above_main_line) != 0:
	h_p = highest_point(above_main_line)
	left_line_highest = create_line(lowest_x, h_p)
	right_line_highest = create_line(highest_x, h_p)
	above_main_line.remove(h_p)
	apexes_above_main_line.append(h_p)

	deleting_points_above_main_line(above_main_line, left_line_highest[0], left_line_highest[1], left_line_highest[2])
	deleting_points_above_main_line(above_main_line, right_line_highest[0], right_line_highest[1], right_line_highest[2])

if len(under_main_line) != 0:
	l_p = lowest_point(under_main_line)
	left_line_lowest = create_line(lowest_x, l_p)
	right_line_lowest = create_line(highest_x, l_p)
	under_main_line.remove(l_p)
	apexes_under_main_line.append(l_p)

	deleting_points_under_main_line(under_main_line, left_line_lowest[0], left_line_lowest[1], left_line_lowest[2])
	deleting_points_under_main_line(under_main_line, right_line_lowest[0], right_line_lowest[1], right_line_lowest[2])

while len(above_main_line) != 0:
	point = highest_point(above_main_line)
	above_main_line.remove(point)
	near_p = nearest_points(apexes_above_main_line, point)
	apexes_above_main_line.append(point)

	l1 = create_line(point, near_p[0])
	l2 = create_line(point, near_p[1])

	deleting_points_above_main_line(above_main_line, l1[0], l1[1], l1[2])
	deleting_points_above_main_line(above_main_line, l2[0], l2[1], l2[2])

while len(under_main_line) != 0:
	point = lowest_point(under_main_line)
	under_main_line.remove(point)
	near_p = nearest_points(apexes_under_main_line, point)
	apexes_under_main_line.append(point)

	l1 = create_line(point, near_p[0])
	l2 = create_line(point, near_p[1])

	deleting_points_under_main_line(under_main_line, l1[0], l1[1], l1[2])
	deleting_points_under_main_line(under_main_line, l2[0], l2[1], l2[2])


apexes_under_main_line.pop(0)
apexes_under_main_line.pop(0)
result = apexes_above_main_line + apexes_under_main_line
print(len(apexes_above_main_line) + len(apexes_under_main_line))
print(result)
