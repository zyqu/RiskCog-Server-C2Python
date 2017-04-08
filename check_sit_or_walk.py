
import sys, os, math

def get_median(lst):
	lst.sort()
	size = len(lst)
	if size == 0:
		return float(0)
	else:
		if size % 2 == 0:
			return (float(lst[size / 2 - 1]) + float(lst[size / 2])) / 2 
		else:
			return float(lst[size / 2]) 

def s2Float(s):
	try:
		return float(s)
	except:
		return 0.0

if __name__=="__main__":
	if len(sys.argv) != 2:
		print "usage : python check_sit_or_walk.py filePath"
		sys.exit(-1)

	filePath = sys.argv[1]
	if not os.path.exists(filePath):
		print "File not exists: %s"%filePath
		sys.exit(-1)

	Gx, Gy, Gz, Ax, Ay, Az, Wx, Wy, Wz = [], [], [], [], [], [], [], [], []
	with open(filePath, 'r') as fobj:
		lines = fobj.readlines()
		count = 0
		for l in lines:
			l = l.strip()
			fVal = s2Float(l)

			if count == 0:
				Ax.append(fVal)
			elif count == 1:
				Ay.append(fVal)
			elif count == 2:
				Az.append(fVal)
			elif count == 3:
				Wx.append(fVal)
			elif count == 4:
				Wy.append(fVal)
			elif count == 5:
				Wz.append(fVal)
			elif count == 6:
				Gx.append(fVal)
			elif count == 7:
				Gy.append(fVal)
			elif count == 8:
				Gz.append(fVal)

			count += 1
			if count == 9:
				count = 0
	
	
	for index in range(len(Ax)):
		Ax[index] = Ax[index] - Gx[index]
		Ay[index] = Ay[index] - Gy[index]
		Az[index] = Az[index] - Gz[index]

	mx, my, mz = get_median(Ax), get_median(Ay), get_median(Az)
	dis = math.sqrt(mx * mx + my * my + mz * mz)
	print "%s\t%s"%(filePath, dis)

	


