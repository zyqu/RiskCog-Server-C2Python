import sys, os
from libxtract import *

data_len = 10
data_cross = 5

def print_XYZ(func, X, Y, Z):
	sys.stdout.write('%0.2f '%func(X))
	sys.stdout.write('%0.2f '%func(Y))
	sys.stdout.write('%0.2f '%func(Z))

def getFloat(str):
	try:
		return float(str)
	except:
		return 0.0

def output(argv, X, Y, Z, wX, wY, wZ, gX, gY, gZ):
	print_XYZ(get_mean,X,Y,Z)
	print_XYZ(get_variance,X,Y,Z)
	print_XYZ(get_standard_deviation,X,Y,Z)
	print_XYZ(get_average_deviation,X,Y,Z)
	print_XYZ(get_skewness,X,Y,Z)
	print_XYZ(get_kurtosis,X,Y,Z)
	print_XYZ(get_zcr,X,Y,Z)
	print_XYZ(get_rms_amplitude,X,Y,Z)
	print_XYZ(get_lowest_value,X,Y,Z)
	print_XYZ(get_highest_value,X,Y,Z)

	sys.stdout.write("%0.2f "%get_result(X,Y,Z))
	
	print_XYZ(get_mean,wX,wY,wZ)
	print_XYZ(get_variance,wX,wY,wZ)
	print_XYZ(get_standard_deviation,wX,wY,wZ)
	print_XYZ(get_average_deviation,wX,wY,wZ)
	print_XYZ(get_skewness,wX,wY,wZ)
	print_XYZ(get_kurtosis,wX,wY,wZ)
	print_XYZ(get_zcr,wX,wY,wZ)
	print_XYZ(get_rms_amplitude,wX,wY,wZ)
	print_XYZ(get_lowest_value,wX,wY,wZ)
	print_XYZ(get_highest_value,wX,wY,wZ)

	sys.stdout.write("%0.2f "%get_result(wX,wY,wZ))
	
	sys.stdout.write("%s "%argv[2])
	sys.stdout.write("%s \n"%argv[3])
	sys.stdout.flush()

if __name__=="__main__":
	if len(sys.argv) != 4:
		print "usage : python make_arff.py filePath belongTo State"
		sys.exit(-1)
	filePath = sys.argv[1]
	if not os.path.exists(filePath):
		print "File not exists: %s"%filePath
		sys.exit(-1)

	vX, vY, vZ, vwX, vwY, vwZ, vgX, vgY,vgZ = [], [], [], [], [], [], [], [], []
	with open(filePath, 'r') as fobj:
		count = 0
		for l in fobj.readlines():
			val = getFloat(l.strip())
			if count == 0:
				vX.append(val)
			elif count == 1:
				vY.append(val)
			elif count == 2:
				vZ.append(val)
			elif count == 3:
				vwX.append(val)
			elif count == 4:
				vwY.append(val)
			elif count == 5:
				vwZ.append(val)
			elif count == 6:
				vgX.append(val)
			elif count == 7:
				vgY.append(val)
			else:
				vgZ.append(val)

			count+=1
			if count == 9:
				count = 0
	l = 0
	while(l + data_len < len(vX)):
		i, j = l, 0
		aX, aY, aZ, awX, awY, awZ, agX, agY, agZ = [], [], [], [], [], [], [], [], []
		while j < data_len:
			aX.append(vX[i])
			aY.append(vY[i])
			aZ.append(vZ[i])
			awX.append(vwX[i])
			awY.append(vwY[i])
			awZ.append(vwZ[i])
			agX.append(vgX[i])
			agY.append(vgY[i])
			agZ.append(vgZ[i])
			i += 1
			j += 1
		l += data_cross
		output(sys.argv,aX,aY,aZ,awX,awY,awZ,agX,agY,agZ)


