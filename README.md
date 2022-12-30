# picturebook.ai

## Todo

1. Extract Data (✅)
2. Train GPT2
3. Build an API for GPT2 and Diffusers (✅, GPT part left).

## Process involved in this:

### Data Extraction

As for the dataset, we use the following websites:

1. for English, extracted the data from the [Gutenberg Website](https://www.gutenberg.org/ebooks/bookshelves/search/?query=children%7Cchristmas%7Cchild%7Cschool).
    - Used the [dataset](https://www.kaggle.com/datasets/mateibejan/15000-gutenberg-books) by [mateibejan](https://www.kaggle.com/mateibejan) to extract the txt files.
    - We took up a subset of the books listed in the dataset.
2. For Tamil, extracted the data from [Siruvarmalar](https://www.siruvarmalar.com/kids-stories-list) and the [Oscar/unshuffled_deduplicated_ta](https://huggingface.co/datasets/oscar/viewer/unshuffled_deduplicated_ta/train) dataset for adding more to the corpus and pretraining.
