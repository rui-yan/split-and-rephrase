# coding=utf-8
# Copyright 2019 The Google Research Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Lint as: python3
"""Calculates evaluation scores for a prediction TSV file.
The prediction file is produced by predict_main.py and should contain 3 or more
columns:
  1: sources (concatenated)
  2: prediction
  3-n: targets (1 or more)
"""
# python3 -m eval_SARI.score_main \
#     --source="/Users/ruiyan/Documents/GitHub/NLP/pred_ref_eval/sources2.txt" \
#     --pred="/Users/ruiyan/Documents/GitHub/NLP/pred_ref_eval/pred_websplit2.txt" \
#     --ref="/Users/ruiyan/Documents/GitHub/NLP/pred_ref_eval/references2.tsv"


from __future__ import absolute_import
from __future__ import division

from __future__ import print_function

from absl import app
from absl import flags
from absl import logging

from eval_SARI import score_lib

FLAGS = flags.FLAGS

flags.DEFINE_string(
    'source', None,
    'text file containing source columns.')
flags.DEFINE_string(
    'pred', None,
    'text file containing prediction columns.')
flags.DEFINE_string(
    'ref', None,
    'TSV file containing target columns.')
flags.DEFINE_bool(
    'case_insensitive', True,
    'Whether score computation should be case insensitive (in the LaserTagger '
    'paper this was set to True).')


def main(argv):
    if len(argv) > 3:
        raise app.UsageError('Too many command-line arguments.')
    flags.mark_flag_as_required('source')
    flags.mark_flag_as_required('pred')
    flags.mark_flag_as_required('ref')

    sources, predictions, target_lists = score_lib.read_data(
        FLAGS.source, FLAGS.pred, FLAGS.ref, FLAGS.case_insensitive)
    logging.info(f'Read file: {FLAGS.source}')
    logging.info(f'Read file: {FLAGS.pred}')
    logging.info(f'Read file: {FLAGS.ref}')
    exact = score_lib.compute_exact_score(predictions, target_lists)
    sari, keep, addition, deletion = score_lib.compute_sari_scores(
        sources, predictions, target_lists)
    print(f'Exact score:     {100*exact:.3f}')
    print(f'SARI score:      {100*sari:.3f}')
    print(f' KEEP score:     {100*keep:.3f}')
    print(f' ADDITION score: {100*addition:.3f}')
    print(f' DELETION score: {100*deletion:.3f}')

if __name__ == '__main__':
  app.run(main)
