#/usr/bin/env bash

base_path=/dfs/scratch0/ruiyan/NLP
dataset=wikisplit

python $base_path/OpenNMT-py@d4ab35a/preprocess.py \
-train_src $base_path/Split-and-Rephrase/data/baseline-seq2seq-${dataset}/train.complex \
-train_tgt $base_path/Split-and-Rephrase/data/baseline-seq2seq-${dataset}/train.simple \
-valid_src $base_path/Split-and-Rephrase/data/baseline-seq2seq-${dataset}/validation.complex \
-valid_tgt $base_path/Split-and-Rephrase/data/baseline-seq2seq-${dataset}/validation.simple \
-save_data $base_path/Split-and-Rephrase/data/baseline-seq2seq-${dataset}/baseline \
-src_seq_length 10000 \
-tgt_seq_length 10000 \
-src_seq_length_trunc 999 \
-tgt_seq_length_trunc 999 \
-dynamic_dict \
-share_vocab \
