#!/usr/bin/env bash
dataset=wikisplit

python3 -m eval_SARI.score_main \
     --source="/Users/ruiyan/Documents/GitHub/NLP/pred_ref_eval/sources2.txt" \
     --pred="/Users/ruiyan/Documents/GitHub/NLP/pred_ref_eval/pred_websplit2.txt" \
     --ref="/Users/ruiyan/Documents/GitHub/NLP/pred_ref_eval/references2.tsv"

