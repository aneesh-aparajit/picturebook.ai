from tokenizers import ByteLevelBPETokenizer
from transformers import GPT2Tokenizer, GPT2Config, GPT2LMHeadModel, DataCollatorForLanguageModelling
from transformers import Trainer, TrainingArguements
from datasets import load_dataset
from glob import glob

data_paths = glob("../../data/data/english/*.txt")

tokenizer = GPT2Tokenizer.from_pretrained('../../pretrained-tokenizers/english')
tokenizer.add_special_tokens({
    "eos_token": "</s>",
    "bos_token": "<s>",
    "unk_token": "<unk>",
    "pad_token": "<pad>",
    "mask_token": "<mask>",
})


config = GPT2Config(
    vocab_size=tokenizer.vocab_size,
    bos_token_id=tokenizer.bos_token_id,
    eos_token_id=tokenizer.eos_token_id
)

model = GPT2LMHeadModel()

data = load_dataset("text", datafiles=data_paths)

def encode(lines):
    return tokenizer(lines['text'], add_special_tokens=True, truncations=True, max_length=128)

data.set_transform(encode)
data = data['train']

data_collator = DataCollatorForLanguageModelling(
    tokenizer=tokenizer,
    mlm=True,
    mlm_probability=0.15,
)

training_args = TrainingArguements(

)
