#! coding: utf-8
import sys, os, random


def insert_func(str, mark):
    insert_pos1 = random.randint(0, len(str))
    while insert_pos1 == 0 or insert_pos1 == len(str):
        insert_pos1 = random.randint(0, len(str))

    str2 = str[:insert_pos1] + mark + str[insert_pos1:]
    return str2, insert_pos1


if __name__ == "__main__":
    inp=sys.argv[1]
    f = open(inp)
    line = f.readline()
    while line:
        item = line.strip().split("\t")
        name = item[0]
        if len(name) <= 3:
            name, pos = insert_func(name, "-")
        else:
            pos = 0
            name, pos = insert_func(name, "-")

            name1 = name[:pos]
            name2 = name[pos:]
            if pos > int(len(name) * 1.0 / 2):
                name1, pos = insert_func(name1, "*")
            else:
                name2, pos = insert_func(name2, "*")
            name = name1 + name2
        print(name)

        line = f.readline()
