from random import randint


def get_datetime(beg, end):
	# yyyy-mm-dd hh:mm:ss
	beg = str_to_arr(beg)
	end = str_to_arr(end)

	count = count_days(beg, end)

	day_ind = randint(1, count)
	date_arr = get_date(beg, day_ind)
	
	time_arr = [randint(0, 23), randint(0, 59), randint(0, 59)]

	datetime = arr_to_str(date_arr + time_arr)

	return datetime


def vis(year):
	if year % 400 == 0:
		return True
	elif year % 100 == 0:
		return False
	elif year % 4 == 0:
		return True
	else:
		return False


def count_days(beg, end):
	b_y, b_m, b_d = beg
	e_y, e_m, e_d = end

	count = 0

	for y in range(b_y, e_y + 1, 1):
		mons = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
		if vis(y):
			mons[1] = 29

		if y == b_y:
			mons[b_m - 1] -= (b_d - 1)
			for i in range(0, b_m - 1):
				mons[i] = 0
		elif y == e_y:
			mons[e_m - 1] = e_d
			for i in range(e_m, 12, 1):
				mons[i] = 0

		count += sum(mons)

	return count


def get_date(beg, ind):
	b_y, b_m, b_d = beg

	count = 0
	y = b_y

	while True:
		mons = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
		if vis(y):
			mons[1] = 29

		if y == b_y:
			mons[b_m - 1] -= (b_d - 1)
			for i in range(0, b_m - 1):
				mons[i] = 0

		for i in range(len(mons)):
			for j in range(mons[i]):
				count += 1
				if count == ind:
					return [y, i + 1, j + 1]

		y += 1


# TRANSFORM
def str_to_arr(str):
	arr = str.split("-")
	return list(map(time_to_int, arr))


def arr_to_str(arr):
	arr = list(map(int_to_time, arr))
	datetime = arr[0] + "-" + arr[1] + "-" + arr[2] +\
	 " " + arr[3] + ":" + arr[4] + ":" + arr[5]

	return datetime


def int_to_time(t):
	t = str(t)

	if len(t) == 1:
		t = "0" + t

	return t


def time_to_int(t):
	if len(t) == 2 and t[0] == "0":
		t = t[1]

	return int(t)
