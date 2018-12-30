import os

def gci(py_list, filepath):
	files = os.listdir(filepath)
	for fi in files:
		fi_d = os.path.join(filepath,fi)            
		if os.path.isdir(fi_d):
			gci(py_list, fi_d)
		else:
			tmp_l = fi.split(".")
			if len(tmp_l) > 1 and tmp_l[1] == "py" :
				py_list.append(fi_d)

if __name__ == "__main__":
	filepath = str(os.getcwd()) + "\dash"
	py_list = []
	gci(py_list, filepath)
	print(len(py_list))