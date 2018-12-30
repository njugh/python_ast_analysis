# -*- coding: utf-8 -*-
import os
import matplotlib.pyplot as plt


def gen_pic(option):
    projects = ["dash", "legit", "tablib"]
    for project in projects:
        f1 = open(os.getcwd() + "\\" + project + "_all\\" + option + "_tree.txt", "r")
        f2 = open(os.getcwd() + "\\" + project + "_all\\" + option + "_str.txt", "r")

        y1 = []
        y2 = []
        for line in f1.readlines():
            y1.append(float(line))
        for line in f2.readlines():
            y2.append(float(line))
        print max(y1)
        print max(y2)

        x = range(1, len(y1)+1)
        plt.figure()
        plt.plot(x, y1)
        plt.xlabel("Commit(times)")
        plt.ylabel("Distance")
        plt.title("AST tree distance")
        plt.savefig(os.getcwd() + "\\" + project + "_all\\" + option + "_tree_distance.png")

        plt.figure()
        plt.plot(x, y2)
        plt.xlabel("Commit(times)")
        plt.ylabel("Distance")
        plt.title("AST str distance")
        plt.savefig(os.getcwd() + "\\" + project + "_all\\" + option + "_str_distance.png")


if __name__ == "__main__":
    options = ["commit", "release"]
    for option in options:
        gen_pic(option)
