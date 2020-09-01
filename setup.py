#!/usr/bin/python
#
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Augment MS-COCO image-caption annotations with the Crisscrossed Captions."""

import argparse
import collections
import csv
import glob
import json


def read_cxc_data(cxc_path, cxc_scores):
  """Read CxC annotations from CSV file.

  Args:
    cxc_path: Path to the CSV file containing CxC scores.
    cxc_scores: Dict of CxC scores mapping caption_id->[(image_id, score,
    rating_type),...] and image_id->[(caption_id, score, rating_type),...].

  Returns:
    Updated list of cxc_scores.
  """
  reader = csv.reader(open(cxc_path, "r"), delimiter=",")
  next(reader)  # Skip header.
  for row in reader:
    caption, image_id, score, rating_type = row
    sent_id = int(caption.split(":")[-1])
    cxc_scores[image_id].append((sent_id, score, rating_type))
    # If the image and caption correspond to the same example, do not append
    # CxC rating twice for the same example.
    if rating_type != "c2i_original":
      cxc_scores[sent_id].append((image_id, score, rating_type))
  return cxc_scores


def read_and_update_coco_data(coco_path, cxc_scores):
  """Read MS-COCO annotations from JSON file and add CxC scores to it.

  Args:
    coco_path: Path to the JSON file containing MS-COCO examples.
    cxc_scores: List of CxC scores from caption_id->(image_id, score,
    rating_type) and image_id->(caption_id, score, rating_type).
  Returns:
    All examples with CxC scores as applicable.
  """
  data = json.load(open(coco_path, "r"))
  for example in data["images"]:
    if example["split"] == "val" or example["split"] == "test":
      image_id = example["filename"]
      if "cxc_scores" not in example:
        example["cxc_scores"] = []
      for item in cxc_scores[image_id]:
        example["cxc_scores"].append(item)
      for sent_id in example["sentids"]:
        for item in cxc_scores[sent_id]:
          example["cxc_scores"].append(item)
  return data


def main(args):
  cxc_scores = collections.defaultdict(list)
  for input_file in glob.glob(args.cxc_input):
    cxc_scores = read_cxc_data(input_file, cxc_scores)
  coco_with_cxc = read_and_update_coco_data(args.coco_input, cxc_scores)
  with open(args.output, "w") as outfile:
    outfile.write(json.dumps(coco_with_cxc))


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument(
      "--coco_input",
      dest="coco_input",
      required=True,
      help="Path to the MS-COCO data.")
  parser.add_argument(
      "--cxc_input",
      dest="cxc_input",
      required=True,
      help="Path pattern to the Crisscrossed Captions (CxC) annotations.")
  parser.add_argument(
      "--output",
      dest="output",
      required=True,
      help="Output file with the augmented COCO and CxC data.")
  main(parser.parse_args())
