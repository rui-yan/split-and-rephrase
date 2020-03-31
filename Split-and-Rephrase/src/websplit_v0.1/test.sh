#!/usr/bin/env bash

base_path=/dfs/scratch0/ruiyan/NLP
dataset=websplit_v0.1
testset=websplit_v0.1
model_file=sprp_onmt_copy_512_acc_87.04_ppl_2.44_e8.pt

python $base_path/OpenNMT-py@d4ab35a/translate.py \
-gpu 1 \
-batch_size 1 \
-model $base_path/phrasing/models/${dataset}/${model_file} \
-src $base_path/Split-and-Rephrase/data/baseline-seq2seq-${testset}/test.complex.unique \
-output $base_path/phrasing/models/${dataset}/${dataset}_test.complex.unique.output \
-beam_size 12 \
-replace_unk

# python ${base_path}/Split-and-Rephrase/src/training_scripts/${model_name}/test.py
