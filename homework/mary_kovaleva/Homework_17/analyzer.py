import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('path', help='Full path to the directory')
parser.add_argument('-t', '--text', help='Text to search')
parser.add_argument('--first', help='Print all lines containing the text', action='store_true')
args = parser.parse_args()


def print_result(filename, line_number, found_text):
    print(f"File: {filename}; Line #{line_number}; Text: {found_text}")


files = os.listdir(args.path)


def get_context():
    for file in files:
        path = os.path.join(args.path, file)
        with open(path, encoding="utf-8") as log:
            for line_num, line in enumerate(log, 1):
                line_words = line.split()
                phrase_words = args.text.split()
                if args.text in line:
                    first_index = line_words.index(phrase_words[0])
                    last_index = line_words.index(phrase_words[-1])
                    start_index = max(0, first_index - 5)
                    end_index = min(len(line_words), last_index + 6)
                    found_text = ' '.join(line_words[start_index: end_index])
                    print_result(file, line_num, found_text)
                    if args.first:
                        return


get_context()
