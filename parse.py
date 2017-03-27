import sys, os

def getKey(item):
	return item[6]

def getHour(s):
	return int(s.split(" ")[1].split(":")[0])

def timeOfDay(s):
	s = s.split(" ")[1]
	tokens = s.split(":")
	res = int(tokens[0]) * 3600 + int(tokens[1]) * 60 + int(tokens[2])
	res = res * 1000 + int(tokens[3])
	return res

def calTime(s1, s2):
	return abs(timeOfDay(s1) - timeOfDay(s2))

def pushSensorVal(vec, lst):
	vec.append(lst[8])
	vec.append(lst[9])
	vec.append(lst[10])

if __name__=="__main__":
	if len(sys.argv) != 2:
		print "usage : python parse.py filePath"
		sys.exit(-1)

	filePath = sys.argv[1]
	if not os.path.exists(filePath):
		print "File not exists: %s"%filePath
		sys.exit(-1)

	data = []
	with open(filePath, 'r') as fobj:
		for l in fobj.readlines():
			l = l.strip()
			tokens = l.split("|")
			if len(tokens) != 11:
				continue
			data.append(tokens)

	data = sorted(data, key=getKey, reverse=False)
	v0, v1, v2 = [], [], []
	for item in data:
		if item[5] == "0":
			v0.append(item)
		elif item[5] == "1":
			v1.append(item)
		elif item[5] == "2":
			v2.append(item)

	l1, l2, cnt = 0, 0, 0
	mp = {}
	for i in range(len(v0)):
		hour = getHour(v0[i][6])
		minVal = calTime(v0[i][6], v1[l1][6])
		for j in range(l1 + 1, len(v1)):
			cal = calTime(v0[i][6], v1[j][6])
			if cal > minVal:
				break
			l1 = j
			minVal = cal

		if minVal > 25:
			continue

		minVal = calTime(v0[i][6], v2[l2][6])
		for j in range(l2 + 1, len(v2)):
			cal = calTime(v0[i][6], v2[j][6])
			if cal > minVal:
				break

			l2 = j
			minVal = cal

		if minVal > 25:
			continue

		if hour not in mp:
			mp[hour] = []
		cnt += 1
		pushSensorVal(mp[hour], v0[i])
		pushSensorVal(mp[hour], v1[l1])
		pushSensorVal(mp[hour], v2[l2])

	for hour in mp:
		lst = mp[hour]
		outputPath = "%s_%s"%(filePath, hour)
		with open(outputPath, "w") as fobj:
			for val in lst:
				fobj.write("%s\n"%val)