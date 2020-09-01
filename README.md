# Crisscrossed Captions

Crisscrossed Captions (CxC) contains 247,315 human-labeled annotations including
positive and negative associations between image pairs, caption pairs and
image-caption pairs.

For more details, please refer the accompanying paper: \
[Crisscrossed Captions: Extended Intramodal and Intermodal Semantic Similarity
Judgments for MS-COCO](https://arxiv.org/abs/2004.15020)

## Motivation

Image captioning datasets have proven useful for multimodal representation
learning, and a common evaluation paradigm based on multimodal retrieval has
emerged. Unfortunately, datasets have only limited cross-modal associations:
images are not paired with others, captions are only paired with others that
describe the same image, there are no negative associations and there are
missing positive cross-modal associations. This undermines retrieval evaluation
and limits research into how inter-modality learning impacts intra-modality
tasks. CxC addresses this gap by extending MS-COCO (dev and test sets from the
Karpathy split) with new semantic similarity judgments.

Below are some examples of caption pairs rated based on
[Semantic Textual Similarity](https://www.aclweb.org/anthology/S12-1051.pdf):

-   Rating 0:

Caption 1: A kite flying in the air over a sand castle.

Caption 2: Scattered people on a wide dry beach including surfers.

-   Rating 1:

Caption 1: Giraffe watching a man push a wheelbarrow loaded with hay.

Caption 2: Two giraffes stand outside of a large building.

-   Rating 2:

Caption 1: A man is sitting on a bench while another takes a nap.

Caption 2: There is an old woman sitting on a bench.

-   Rating 3:

Caption 1: A train is driving down the tracks in front of a building.

Caption 2: A purple and yellow train traveling down train tracks.

-   Rating 4:

Caption 1: A cut pizza and a glass on a table.

Caption 2: Small pizza sits on a plate on a restaurant table.

-   Rating 5:

Caption 1: A family of sheep standing next to each other on a lush green field.

Caption 2: A herd of sheep standing next to each other on a lush green field.

## Structure of the data

There are 2 CSV files per task (STS, SIS, SITS) and per split (val, test): one
with raw annotator scores ('*_raw.csv') and one with aggregated scores per
example. The first two columns represent the IDs from MS-COCO for the
corresponding image or caption, followed by the annotation score. The last
column indicates the method in which the example was sampled:

-   STS:

c2c_cocaption: caption pairs from the same MS-COCO example

c2c_isim: caption pairs from different MS-COCO examples sampled based on image
similarity

-   SIS:

i2i_csim: image pairs from different MS-COCO examples sampling based on caption
similarity.

-   SITS:

c2i_intrasim: caption-image pairs from different MS-COCO examples.

c2i_original: caption-image pairs from the same MS-COCO examples.

## Examples

Following are some examples for each task:

-   STS:

    *   Rating 1:

        *   An old car sitting on top of a lush green field.
        *   A couple of motorcycles parked next to each other.

    *   Rating 3:

        *   A yellow tray topped with a cup of coffee and a donut.
        *   A white plate topped with donuts sitting on a stove top.

    *   Rating 5:

        *   A man standing on a tennis court holding a racquet.
        *   A man standing on a tennis court holding a tennis racquet.

-   SIS:

    *   Rating 1:

        ![SIS Rating 1](images/sis_rating_1_0.png "SIS Rating 1")
        ![SIS Rating 1](images/sis_rating_1_1.png "SIS Rating 1")

    *   Rating 3:

        ![SIS Rating 3](images/sis_rating_3_0.png "SIS Rating 3")
        ![SIS Rating 3](images/sis_rating_3_1.png "SIS Rating 3")

    *   Rating 5:

        ![SIS Rating 5](images/sis_rating_5_0.png "SIS Rating 5")
        ![SIS Rating 5](images/sis_rating_5_1.png "SIS Rating 5")

-   SITS:

    *   Rating 1:

        A man in a hat rides an elephant in a river.

        ![SITS Rating 1](images/sits_rating_1.png "SITS Rating 1")

    *   Rating 3:

        A man is riding a surfboard at the beach.

        ![SITS Rating 3](images/sits_rating_3.png "SITS Rating 3")

    *   Rating 5:

        A man poses with a surfboard on a beach.

        ![SITS Rating 5](images/sits_rating_5.png "SITS Rating 5")

## Augment MS-COCO examples with CxC labels

Download the MS-COCO Karpathy split annotations (from
[here](https://cs.stanford.edu/people/karpathy/deepimagesent)) and pass them as
`coco_input` in the following merge script:

```
python -m crisscrossed_captions/setup --coco_input "/path/to/coco/json" --cxc_input "/path/to/cxc/sits/*" --output "/path/to/combined/json"
```

## Reference

If you use or discuss this dataset in your work, please cite our paper:

```
@article{parekh2020crisscrossed,
  title={Crisscrossed Captions: Extended Intramodal and Intermodal Semantic Similarity Judgments for MS-COCO},
  author={Parekh, Zarana and Baldridge, Jason and Cer, Daniel and Waters, Austin and Yang, Yinfei},
  journal={arXiv preprint arXiv:2004.15020},
  year={2020}
}
```

## Contact

If you have a technical question regarding the dataset or publication, please
create an issue in this repository.
