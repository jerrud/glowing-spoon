import pyperclip
import xml.etree.ElementTree as ET
tree = ET.parse('E:\Sutter 30 Bed\XML\L2 Facilitated Model 03-04-19.xml')
root = tree.getroot()

test_name = []
test_new = []
test_reviewed = []
test_active = []
test_approved = []
test_resolved = []

for x in root.iter('clashtest'):
    test_name.append(x.get('name'))

for x in root.iter('summary'):
    test_new.append(x.get('new'))

for x in root.iter('summary'):
    test_reviewed.append(x.get('reviewed'))

for x in root.iter('summary'):
    test_active.append(x.get('active'))

for x in root.iter('summary'):
    test_approved.append(x.get('approved'))

for x in root.iter('summary'):
    test_resolved.append(x.get('resolved'))

xml_results = zip(test_name,test_new,test_reviewed,test_active,test_approved,test_resolved)

xml_results_list = list(xml_results)

def print_lists (my_list = [], *args):
    print("| Test Name | New | Reviewed | Active | Approved | Resolved |")
    print("|:---|:----:|:----:|:----:|:----:|:---: |")
    for x in my_list:
        print(f"|{x[0]}|{x[1]}|{x[2]}|{x[3]}|{x[4]}|{x[5]}|")
    if args:
        arg_list = args
        for x in arg_list:
            print(f"|{x[0]}|{x[1]}|{x[2]}|{x[3]}|{x[4]}|{x[5]}|")

print_lists(xml_results_list)
