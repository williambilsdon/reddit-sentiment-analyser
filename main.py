import argparse
import spacy

def main(message: str):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(message)
    filtered_list = [word.text for word in doc if word.is_stop is False]
    print(filtered_list)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--message", "-m",required=True,help="Provide a message to have it's positivity evaluated")
    args=parser.parse_args()
    main(args.message)