import os
import re
import csv
'''
The files should be parallel line for line.
- predictions: system output for decomposing a sentence into one or more simpler
    sentences. (The code refers to each such simpler sentence as a parcel.)
    Format:
        parcel_1 SEP parcel_2 ...
    For example, a decomposition of "I think , therefore I am ." into two
    sentences (parcels) should be represented as:
        I think . <::::> Therefore I am .
- gold: ground truth decomposition(s) for the corresponding line.
    Format:
        decomposition_1 <TAB> decomposition_2 [<TAB> decomposition_3 ...]
      where each decomposition has the format
         parcel_1 SEP parcel_2 ...
    Example of two alternative reference decompositions:
         I think . <::::> Therefore I am . <TAB> I think . <::::> Thus I am .
'''

source_fname="sources2_100.txt"
input1_fname="pred_websplit2_100.txt"
input2_fname="pred_wikisplit2_100.txt"

out_fname="F8.csv"

source=""
input1=""
input2=""
data_list=[]

with open(source_fname, 'r') as h1:
    for line in h1:
        line = re.sub(r'\s([,?.!"](?:\s|$))', r'\1', line)
        source += line
    h1.close()

with open(input1_fname, 'r') as h2:
    for line in h2:
        line = re.sub(r'\s([,?.!"](?:\s|$))', r'\1', line)
        input1 += line
    h2.close()

with open(input2_fname, 'r') as h3:
    for line in h3:
        line = re.sub(r'\s([,?.!"](?:\s|$))', r'\1', line)
        input2 += line
    h3.close()

source = source.splitlines()
input1 = input1.splitlines()
input2 = input2.splitlines()

for i in range(len(source)):
    data_list.append([source[i], input1[i], input2[i]])

# # print(data_list)
# print(data_list[1])
with open(out_fname, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Source", "Input1", "Input2"])
    for i in range(len(data_list)):
        writer.writerow([row for row in data_list[i]])
