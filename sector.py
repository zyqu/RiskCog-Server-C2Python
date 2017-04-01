import sys, os, random
sector = 300
attribute = ["Xmean", "Ymean", "Zmean", "Xvariance", "Yvariance",
		"Zvariance", "XstdDev", "YstdDev", "ZstdDev", "XavgDev", "YaveDev",
		"ZavgDev", "Xskewness", "Yskewness", "Zskewness", "Xkurtosis",
		"Ykurtosis", "Zkurtosis", "Xzcr", "Yzcr", "Zzcr", "Xrms", "Yrms",
		"Zrms", "Xlowest", "Ylowest", "Zlowest", "Xhighest", "Yhighest",
		"Zhighest", "Result", "wXmean", "wYmean", "wZmean", "wXvariance",
		"wYvariance", "wZvariance", "wXstdDev", "wYstdDev", "wZstdDev",
		"wXavgDev", "wYaveDev", "wZavgDev", "wXskewness", "wYskewness",
		"wZskewness", "wXkurtosis", "wYkurtosis", "wZkurtosis", "wXzcr",
		"wYzcr", "wZzcr", "wXrms", "wYrms", "wZrms", "wXlowest", "wYlowest",
		"wZlowest", "wXhighest", "wYhighest", "wZhighest", "wResult", "USER",
		"STATE"]

def getFloat(s):
	try:
		return float(s)
	except:
		return None

def input_1(fname, data):
	start = 1
	with open(fname, 'r') as fobj:
		for l in fobj.readlines():
			l = l.strip()
			if len(l) == 0:
				continue

			v = []

			if l == "@data":
				start = 1
				continue

			if start == 0:
				continue

			for i in range(len(name_map) - 2):
				floatVal = getFloat(l)
				if l != None:
					v.append(floatVal)

			v.append(1)
			v.append(0)
			if len(v) != 0:
				data.append(v)

def input_500(fname, data, rest):
	start, cnt = 1, 0
	get_num = min(sector, rest)
	with open(fname, 'r') as fobj:
		for l in fobj.readlines():
			l = l.strip()
			if len(l) == 0:
				continue
			if get_num <= 0:
				break

			v = []
			if l == "@data":
				start = 1
				continue

			get_num -= 1
			cnt += 1
			for i in range(len(name_map) - 2):
				floatVal = getFloat(l)
				if l != None:
					v.append(floatVal)
			v.append(1)
			v.append(0)
			if len(v) != 0:
				data.append(v)							

	return cnt

def print_replace(lst, replace):
	lst[name_map["USER"]] = replace
	for i in range(len(name_map) - 2):
		sys.stdout.write("%0.2f "%lst[i])
	sys.stdout.write("%s %s\n "%(replace, 0))
	sys.stdout.flush()


if __name__=="__main__":
	if len(sys.argv) != 3:
		print "usage : python sector.py imei ratio"
		sys.exit(-1)
	try:
		imei = sys.argv[1]
		oratio = int(sys.argv[2])
	except:
		print "usage : python sector.py imei ratio"
		sys.exit(-1)		

	name_map = {}
	num_of_attribute = len(attribute)
	for i in range(num_of_attribute):
		name_map[attribute[i]] = i

	one_points, five_points = [], []
	files = []
	if not os.path.exists("files"):
		print "File not exists: files"
		sys.exit(-1)

	with open("files", 'r') as fobj:
		for l in fobj.readlines():
			l = l.strip()
			if len(l) > 0:
				files.append(l)

	for ff in files:
		if ff.find(imei) >= 0 and os.path.exists(ff):
			input_1(ff, one_points)

	rest = len(one_points) * oratio
	file_set = set()
	while rest > 0:
		rand_file_name = files[random.randint(0, len(files) - 1)]
		while (rand_file_name in file_set or rand_file_name.find(imei) < 0):
			rand_file_name = files[random.randint(0, len(files) - 1)]
		file_set.add(rand_file_name)
		rest -= input_500(rand_file_name, five_points, rest)

	for item in one_points:
		print_replace(item, 1)

	for item in five_points:
		print_replace(item, 0)



