import argparse
import spacy

def main(message: str):
    nlp = spacy.load("en_core_web_sm")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--message", "-m",required=True,help="Provide a message to have it's positivity evaluated")
    args=parser.parse_args()
    main(args.message)