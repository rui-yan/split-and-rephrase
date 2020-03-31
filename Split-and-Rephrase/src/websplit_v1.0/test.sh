#!/usr/bin/env bash

base_path=/dfs/scratch0/ruiyan/NLP
dataset= websplit_v1.0

model_file=sprp_onmt_copy_512_acc_54.76_ppl_10.26_e1.pt

python $base_path/OpenNMT-py@d4ab35a/translate.py \
-gpu 1 \
-batch_size 1 \
-model $base_path/phrasing/models/${dataset}/${model_file} \
-src $base_path/Split-and-Rephrase/data/baseline-seq2seq-${dataset}/test.complex.unique \
-output $base_path/phrasing/models/${dataset}/test.complex.unique.output \
-beam_size 12 \
-replace_unk

# python ${base_path}/Split-and-Rephrase/src/training_scripts/${model_name}/test.py
