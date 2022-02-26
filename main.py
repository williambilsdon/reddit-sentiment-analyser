import argparse
import nltk

def main(message: str):
    tokenized_message = nltk.word_tokenize(message)
    print(tokenized_message)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--message", "-m",required=True,help="Provide a message to have it's positivity evaluated")
    args=parser.parse_args()
    main(args.message)