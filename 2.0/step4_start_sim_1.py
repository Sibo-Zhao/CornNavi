import xml.etree.ElementTree as ET


def get_offsprings(os_path, mom, dad):

    with open(os_path, "rt") as f:
        tree = ET.parse(f)
        root = tree.getroot()
        sublist_elements = root.findall('list')[mom][dad]
        return sublist_elements.text


path = "../file_ignore/offsprings.xml"
o_set = {}
