import os
import re

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

org_fname = "/Users/ruiyan/Documents/GitHub/NLP/pred_ref_eval/pred_websplit2.txt"
mod_fname = "/Users/ruiyan/Documents/GitHub/NLP/pred_ref_eval/pred_websplit2.txt"

lines = ""

with open(org_fname, 'r') as fhand:
    for line in fhand:
        newline = re.sub(r' \. ',  r' . <::::> ', line)
        lines += newline.strip()+"\n"
    fhand.close()

with open(mod_fname, 'w') as fhand2:
    fhand2.write(lines)
    fhand2.close()

