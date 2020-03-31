lines_seen = set() # holds lines already seen
outfname = "Split-and-Rephrase/data/baseline-seq2seq-websplit_v1.0/validation.complex.unique"
infname = "Split-and-Rephrase/data/baseline-seq2seq-websplit_v1.0/validation.complex"
outfile = open(outfname, "w")
for line in open(infname, "r"):
    if line not in lines_seen: # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
outfile.close()

