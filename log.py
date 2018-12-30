# -*- coding: utf-8 -*-
import os


def gen_commit():
	projects = ["dash", "legit", "tablib"]
	for project in projects:
		fp = open(os.getcwd() + "\\" + project +"_all" + "\log.txt", "r")
		fc = open(os.getcwd() + "\\" + project +"_all" + "\commit.txt", "w")
		commit_list = []
		for line in fp.readlines():
			if line.startswith("commit"):
				commit_num = line.split(" ")[1]
				commit_list.append(commit_num)
		print len(commit_list)

		commit_list.reverse()
		for i in commit_list:
			fc.write(i)

		fp.close()
		fc.close()

if __name__ == "__main__":
	gen_commit()