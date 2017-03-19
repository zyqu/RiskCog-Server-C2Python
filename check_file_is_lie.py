from check_sit_or_walk import get_median
from check_sit_or_walk import s2Float

import sys, os, math

if __name__=="__main__":
	if len(sys.argv) != 2:
		print "usage : python check_file_is_lie.py filePath"
		sys.exit(-1)
	
	filePath = sys.argv[1]
	if not os.path.exists(filePath):
		print "File not exists: %s"%filePath
		sys.exit(-1)

	Gx, Gy, Gz, Ax, Ay, Az, Wx, Wy, Wz = [], [], [], [], [], [], [], [], []
	with open(filePath, 'r') as fobj:
		lines = fobj.readlines()
		count = 0
		for index in range(len(lines)):
			fVal = s2Float(lines[index].strip())
			if fVal == None:
				continue

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
	gx = abs(get_median(Gx))
	gy = abs(get_median(Gy))
	gz = abs(get_median(Gz))
	if gx <= 1.5 and gy <= 1.5 and gz < 10 and gz >= 9:
		print "%s"%filePath


