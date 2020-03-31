#!/usr/bin/env bash

base_path=/dfs/scratch0/ruiyan/NLP
dataset=websplit_v0.1
model_name=sprp_onmt_copy_512

python $base_path/OpenNMT-py@d4ab35a/train.py \
-save_model $base_path/phrasing/models/${dataset}/${model_name} \
-data $base_path/Split-and-Rephrase/data/baseline-seq2seq-${dataset}/baseline \
-copy_attn \
-copy_attn_force \
-global_attention mlp \
-word_vec_size 512 \
-rnn_size 512 \
-layers 1 \
-encoder_type brnn \
-epochs 30 \
-seed 777 \
-batch_size 32 \
-max_grad_norm 2 \
-share_embeddings \
-gpuid 0 \
-start_checkpoint_at 1

