#!/usr/bin/env bash
dataset=wikisplit2
python3 -m eval_BLEU.score_main \
    --gold="/Users/ruiyan/Documents/GitHub/NLP/pred_ref_eval/references2.tsv" \
    --pred="/Users/ruiyan/Documents/GitHub/NLP/pred_ref_eval/pred_websplit2.txt"

