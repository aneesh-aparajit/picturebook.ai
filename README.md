# picturebook.ai

The idea is to build an AI generated picture book. The main functionality of this product to generate stories from a starting part of a sentence or from a set of keywords given in a specific set of languages.

Essentially, this is a generative model which can generate **new** stories and we with the help of "**Diffusion Models**", we generate images to add the "pictures" in the "picturebook".

This repository should generate stories in the following languages as of now (will add more as and when I get time):-

1. English
2. Tamil

## Process involved in this:

### Data Extraction

As for the dataset, we use the following websites:

1. for English, we extract the data from the [Gutenberg Website](https://www.gutenberg.org/ebooks/bookshelves/search/?query=children%7Cchristmas%7Cchild%7Cschool).
2. For Tamil, we extract the data from [Siruvarmalar](https://www.siruvarmalar.com/kids-stories-list) and the [Oscar/unshuffled_deduplicated_ta](https://huggingface.co/datasets/oscar/viewer/unshuffled_deduplicated_ta/train) dataset for adding more to the corpus and pretraining.

### GPT2 Training

For the training GPT2, we expect to train 2 different GPT2 models, one for English and one for Tamil.

### Image Generation

For the generation, we will use the [CompVis/stable-diffusion-v1-4](https://huggingface.co/CompVis/stable-diffusion-v1-4) from the `diffusers` module.

### Deployment

Deployment would be most probably based on FastAPI/Flask with React.
