import os
import numpy as np
import matplotlib.pyplot as plt

txt_files = list()
xlsx_files = list()
python_files = list()
lnk_files = list()
other_files = list()

path = '.'
other = ['.py','.txt','.xlsx','.lnk']

for fil in os.listdir(path):
    if fil.endswith(".txt"):
        txt_files.append(fil)
    if fil.endswith(".xlsx"):
        xlsx_files.append(fil)
    if fil.endswith(".py"):
        python_files.append(fil)
    if fil.endswith(".lnk"):
        lnk_files.append(fil)
    if not fil.endswith(tuple(other)):
        other_files.append(fil)

txt_lg = len(txt_files)
xlsx_lg = len(xlsx_files)
py_lg = len(python_files)
lnk_lg = len(lnk_files)
other_lg = len(other_files)

#print("Total txt files : " + str(txt_lg))
#print("Total xlsx files : " + str(xlsx_lg))
#print("Total python files : " + str(py_lg))
#print("Total lnk files : " + str(lnk_lg))
#print("Total other files : " + str(other_lg))


#Graph
height = [txt_lg,xlsx_lg,py_lg,lnk_lg,other_lg]
bars = ('txt files', 'xlsx files', 'Py files', 'Links', 'Others')
plt.bar(bars, height, color=(0.2, 0.4, 0.6, 0.6), width=0.5)

# Custom Axis titles
plt.xlabel('Files Extensions', fontweight='bold', color = 'blue', fontsize='10', horizontalalignment='center')
plt.ylabel('Files Count', fontweight='bold', color = 'blue', fontsize='10', horizontalalignment='center')

for i,v in enumerate(height):
    plt.text(i,v, str(v))
    
#Show the plot 
plt.show()
