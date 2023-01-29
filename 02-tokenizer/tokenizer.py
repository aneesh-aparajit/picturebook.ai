from tokenizers import ByteLevelBPETokenizer
from glob import glob
import os
import config

def train_tokenizer(path, save_path):
    tokenizer = ByteLevelBPETokenizer()
    tokenizer.train(
        files=path, 
        vocab_size=52_000, 
        min_frequency=2, 
        special_tokens=['<s>', '<pad>', '</s>', '<unk>', '<mask>']
    )
    tokenizer.save(save_path)


if __name__ == '__main__':
    english_paths = glob(os.path.join(config.ENGLISH_PATH, '*.txt'))
    tamil_paths = glob(os.path.join(config.TAMIL_PATH, '*.txt'))

    print(f'TRAINING TOKENIZER FOR ENGLISH...')
    print(f'tokenizing: {len((english_paths))} files.')
    train_tokenizer(path=english_paths, save_path=config.ENGLISH_TOKENIZER_PATH)

    print(f'TRAINING TOKENIZER FOR TAMIL...')
    print(f'tokenizing: {len((tamil_paths))} files.')
    train_tokenizer(path=tamil_paths, save_path=config.TAMIL_TOKENIZER_PATH)

    print(f'DONE!')
