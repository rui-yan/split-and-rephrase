# pick 100 rows without -LRB- and R

import random
random.seed(10)

indices = []
lines = []

infname = "pred_wikisplit2.txt"
infname2 = "chosen_indices.txt"
outfname = "pred_wikisplit2_100.txt"

for line in open(infname, "r"):
    lines.append(line)

for line in open(infname2, "r"):
    indices.append(int(line))

# while len(indices) != 100:
#     r = random.randint(1,929)
#     if r not in indices:
#         indices.append(r)

# indices = sorted(indices)
# with open(infname2, "w") as f:
#     for i in range(len(indices)):
#         f.write(str(indices[i])+'\n')
#     f.close()

chosen = [lines[i] for i in indices]

with open(outfname, "w") as f:
    for line in chosen:
        f.write(line)
    f.close()

