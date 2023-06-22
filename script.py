import re
import nltk
import sys
import argparse
import os
import time


def is_name(word):
    return word.capitalize() in names


def create_dictionary(text_file, word_min_length_threshold):
    word_set = set()
    pattern = re.compile(r'\b\w+\b')
    with open(text_file, 'r') as file:
        for line in file:
            words = pattern.findall(line)
            for word in words:
                if word.isnumeric() or len(word) < word_min_length_threshold:
                    continue
                if is_name(word):
                    word += "(name)"
                word_set.add(word.lower())

    word_counts = {}
    for word in word_set:
        word_counts[word] = 0

    with open(text_file, 'r') as file:
        for line in file:
            words = pattern.findall(line)
            for word in words:
                if word.lower() in word_counts:
                    word_counts[word.lower()] += 1

    return dict(sorted(word_counts.items(), key=lambda item: item[1], reverse=True))


def create_html(sorted_dictionary, output_file, google_translate_to=None):
    with open(output_file, 'w') as file:
        file.write('<html>\n<head>\n</head>\n<body>\n')
        file.write('<table style="text-align: center; font-size: 15px; font-family: monospace; border-collapse: collapse;">\n')
        file.write('<tbody>\n<tr style="background-color: #E4EFE7;">\n<th>Index</th>\n<th>Word</th>\n<th>Occurrences</th>\n<th>Definition</th>\n</tr>\n')

        for i, (word, rank) in enumerate(sorted_dictionary.items(), start=1):
            tr_style = "background-color: #ece4d5a8;" if i % 2 == 0 else ""
            file.write(f'<tr style="{tr_style}">\n<td>{i}</td>\n<td><strong>{word}</strong></td>\n<td>{rank}</td>\n')
            file.write(f'<td>\n<a href="https://www.oxfordlearnersdictionaries.com/definition/english/{word}?q={word}" target="_blank"><img src="./images/OUP.png" alt="OUP" width="20" height="20"></a>\n')
            file.write(f'<a href="https://dictionary.cambridge.org/dictionary/learner-english/{word}" target="_blank"><img src="./images/CUP.png" alt="CUP" width="20" height="20"></a>\n')
            file.write(f'<a href="https://www.britannica.com/dictionary/{word}" target="_blank"><img src="./images/Britannica.png" alt="Britannica" width="20" height="20"></a>\n')
            file.write(f'<a href="https://www.ldoceonline.com/dictionary/{word}" target="_blank"><img src="./images/Longman.png" alt="Longman" width="20" height="20"></a>\n')
            file.write(f'<a href="https://www.macmillandictionary.com/dictionary/american/{word}" target="_blank"><img src="./images/mac.png" alt="macmillan" width="20" height="20"></a>\n')
            file.write(f'<a href="https://en.wiktionary.org/wiki/{word}" target="_blank"><img src="./images/Wiki.png" alt="Wiktionary" width="20" height="20"></a>\n')
            file.write(f'<a href="https://sentencedict.com/{word}.html" target="_blank"><img src="./images/Sentence.png" alt="Sentencedict.com" width="20" height="20"></a>\n')
            if google_translate_to:
                file.write(f'<a href="https://translate.google.com/?sl=en&tl={google_translate_to}&text={word}&op=translate" target="_blank"><img src="./images/GoogleTranslate.png" alt="Sentencedict.com" width="20" height="20"></a>\n')
            file.write('</td>\n</tr>\n')

        file.write('</tbody>\n</table>\n</body>\n</html>')


if __name__ == "__main__":
    start_time = time.time()
    parser = argparse.ArgumentParser()
    parser.add_argument("text_file", help="Path to the input text file")
    parser.add_argument("output_file", help="Path to the output HTML file")
    parser.add_argument("--min_length_threshold", type=int,
                        default=4, help="Word min length threshold (default: 4)")
    parser.add_argument("--google_translate_to",
                        help="Destination language for translation (e.g., 'fa' for Farsi)")
    args = parser.parse_args()

    if not os.path.isfile(args.text_file):
        print(f"Error: Input file '{args.text_file}' does not exist")
        sys.exit(1)

    output_directory = os.path.dirname(args.output_file)

    if output_directory != "" and not os.path.exists(output_directory):
        print(f"Error: Output directory '{output_directory}' does not exist")
        sys.exit(1)

    nltk.download('names')
    names = set(nltk.corpus.names.words())

    sorted_dictionary = create_dictionary(
        args.text_file, args.min_length_threshold)
    create_html(sorted_dictionary, args.output_file, args.google_translate_to)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.2f} seconds")
