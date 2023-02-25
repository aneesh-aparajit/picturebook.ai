import os
from tokenizers.models import BPE
from tokenizers import Tokenizer
from tokenizers.decoders import ByteLevel as ByteLevelDecoder
from tokenizers.normalizers import NFKC, Sequence
from tokenizers.pre_tokenizers import ByteLevel
from tokenizers.trainers import BpeTrainer
from glob import glob


class BPETokenizer(object):
    def __init__(self):
        self.tokenizers = Tokenizer(BPE())
        self.tokenizer.normalizer = Sequence([NFKC])
        self.tokenizer.pre_tokenizer = ByteLevel()
        self.tokenizer.decode = ByteLevelDecoder()

    def train(self, paths):
        trainer = BpeTrainer(
            vocab_size=52_000,
            show_progress=True,
            min_frequency=2,
            special_tokens=["<s>", "<pad>", "</s>", "<unk>", "<mask>"],
            initial_alphabet=ByteLevel.alphabet()
        )
        self.tokenizer.train(trainer=trainer, files=paths)

    def save(self, path):
        if not os.path.exists(path):
            os.mkdir(path)
        self.tokenizer.model.save(path)


if __name__ == '__main__':
    english_paths = glob('../../../data/data/english/*.txt')
    tamil_paths = glob('../../../data/data/tamil/*.txt')

    tokenizer = BPETokenizer()
    tokenizer.train(english_paths)
    save_path = '../../../pretrained-tokenizers/english/'
    tokenizer.save(save_path)

    tokenizer = BPETokenizer()
    tokenizer.train(english_paths)
    save_path = '../../../pretrained-tokenizers/tamil/'
    tokenizer.save(save_path)
