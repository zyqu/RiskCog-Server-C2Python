import sys, os

CUR_PATH = os.path.dirname(os.path.realpath(__file__))
LOG_PATH = os.path.join(CUR_PATH, "log")
OUT_PATH = os.path.join(CUR_PATH, "out")

if __name__=="__main__":
	if not os.path.exists(LOG_PATH):
		print "File not exists %s"%LOG_PATH
		sys.exit(-1)
	
	try:
		thres = float(sys.argv[1])
	except:
		print "usage : python deternmine.py threshold[float]"
		sys.exit(-1)		

	with open(LOG_PATH, 'r') as fin:
		with open(OUT_PATH, 'w') as fout:
			for l in fin.readlines():
				l = l.strip()
				tokens = l.split("\t")
				fpath = tokens[0]
				val = float(tokens[1].split(" ")[0])
				if val > thres:
					fout.write("%s %s\n"%(fpath, "walk"))
				else:
					fout.write("%s %s\n"%(fpath, "sit"))