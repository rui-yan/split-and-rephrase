import os
import re

org_fname = "/Users/ruiyan/Documents/GitHub/NLP/pred_ref_eval/pred_websplit2.txt"
mod_fname = "/Users/ruiyan/Documents/GitHub/NLP/pred_ref_eval/pred_websplit2_clean.txt"

lines = ""

with open(org_fname, 'r') as fhand:
    for line in fhand:
        newline = re.sub(r' . <::::> ',  r'. ', line)
        newline = re.sub(r'\s([?.!"](?:\s|$))', r'\1', newline)
        lines += newline.strip()+"\n"
    fhand.close()

with open(mod_fname, 'w') as fhand2:
    fhand2.write(lines)
    fhand2.close()
