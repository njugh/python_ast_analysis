# -*- coding: utf-8 -*
# git rev-parse HEAD表示查看当前commit版本

import os
import Levenshtein
from find_file import gci
from process import process_file


def gen_dist(project):
    fp = open(os.getcwd() + "\\" + project +"_all\\"+ "release.txt", "r")
    release_list = []
    for line in fp.readlines():
        release_list.append(line)
    os.chdir(os.getcwd() + "\\" + project +"_all\\" + project)
    print "当前工作目录：", os.getcwd()
    os.system("git checkout " + release_list[0])
    print "切换到初始commit，当前版本：", os.system("git rev-parse HEAD")

    pre = 0
    now = pre + 1

    old_py_files = []
    old_py_files_tree = {}
    old_py_files_str = {}

    new_py_files = []
    new_py_files_tree = {}
    new_py_files_str = {}

    tree_dists = []
    str_dists = []
    gci(old_py_files, str(os.getcwd()))
    for f in old_py_files:
        f_tree, f_str = process_file(f)
        old_py_files_tree[f] = f_tree
        old_py_files_str[f] =  f_str

    llen = len(release_list)
    while now < llen:
        os.system("git checkout " + release_list[now])
        print "Release：", now, " ", os.system("git rev-parse HEAD")
        gci(new_py_files, str(os.getcwd()))
        for f in new_py_files:
            f_tree, f_str = process_file(f)
            new_py_files_tree[f] = f_tree
            new_py_files_str[f] = f_str

        # dist
        t_dist = 0
        s_dist = 0
        same_files = [f for f in old_py_files if f in new_py_files]
        del_files = [f for f in old_py_files if f not in new_py_files]
        add_files = [f for f in new_py_files if f not in old_py_files]

        for f in same_files:
            t_dist += Levenshtein.distance(old_py_files_tree[f], new_py_files_tree[f])
            s_dist += Levenshtein.distance(old_py_files_str[f], new_py_files_str[f])

        for f in del_files:
            t_dist += Levenshtein.distance(old_py_files_tree[f], '')
            s_dist += Levenshtein.distance(old_py_files_str[f], '')

        for f in add_files:
            t_dist += Levenshtein.distance('', new_py_files_tree[f])
            s_dist += Levenshtein.distance('', new_py_files_str[f])

        tree_dists.append(t_dist)
        str_dists.append(s_dist)

        pre = now
        now = pre + 1
        old_py_files = new_py_files[:]
        old_py_files_tree = new_py_files_tree.copy()
        old_py_files_str = new_py_files_str.copy()
        new_py_files[:] = []
        new_py_files_tree.clear()
        new_py_files_str.clear()

    print tree_dists
    print str_dists

    parent_path = os.path.dirname(str(os.getcwd()))
    f1 = open(parent_path + "\\release_tree.txt", "w")
    f2 = open(parent_path + "\\release_str.txt", "w")
    for i in tree_dists:
        f1.write(str(i)+'\n')
    for i in str_dists:
        f2.write(str(i)+'\n')
    f1.close()
    f2.close()

    os.chdir(os.path.dirname(parent_path))


if __name__ == "__main__":
    projects = ["dash", "legit", "tablib"]
    for project in projects:
        gen_dist(project)

