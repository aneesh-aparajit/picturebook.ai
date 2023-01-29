from transformers import GPT2Tokenizer
import config


if __name__ == '__main__':
    tokenizer = GPT2Tokenizer.from_pretrained(config.ENGLISH_TOKENIZER_PATH)

    while True:
        text = input("Enter string to tokenize: ")
        tok = tokenizer(text)
        print(tok)

        cont = input("do you want to continue: ")
        if cont == "no":
            break

