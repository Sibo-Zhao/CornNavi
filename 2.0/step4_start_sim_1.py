import xml.etree.ElementTree as ET
import os, pickle
from itertools import combinations

"""
[0,0,0,0,2,2]: 8
[0,0,2,2,2,0]: 78
[2,2,0,0,0,0]: 648
"""

def get_offsprings(os_path, mom, dad):

    with open(os_path, "rt") as f:
        tree = ET.parse(f)
        root = tree.getroot()
        sublist_elements = root.findall('list')[mom][dad]
        return eval(sublist_elements.text)


path = "../file_ignore/offsprings.xml"
o_set = {8, 78, 648}
try:
    os.mkdir("F1")
    print("文件夹已创建！")
except FileExistsError:
    print("文件夹已存在。")

combs = combinations(o_set, 2)
times = 1
for comb in combs:
    # print(get_offsprings(path, comb[0], comb[1]))
    new_set = set(get_offsprings(path, comb[0], comb[1])).union(o_set)
    with open("F1/{}_{}_F1_{}".format(comb[0], comb[1], times), 'xb') as f:
        try:
            pickle.dump(new_set, f)
        except FileExistsError:
            print("文件夹已存在。")
    times += 1


if __name__ == '__main__':
    print("sunoneeye")
