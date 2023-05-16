import numpy as np
import xml.etree.ElementTree as ET
import pickle


def b():

    with open('population.pickle', 'rb') as f:
        p = pickle.load(f)

    rules = np.load('rules.npy')

    arr = [[None for j in range(len(p))] for i in range(len(p))]

    for i in range(len(p)):
        for j in range(len(p)):
            temp = []
            for k in range(len(p)):
                if rules[i][j][k] != 0:
                    temp.append(k)
            arr[i][j] = temp

    root = ET.Element("data")

    for sublist in arr:
        subelement = ET.SubElement(root, "list")
        for item in sublist:
            item_element = ET.SubElement(subelement, "item")
            item_element.text = str(item)

    tree = ET.ElementTree(root)
    tree.write('offsprings.xml')


if __name__ == '__main__':
    print("sunoneeye")
