import os
import re
from pathlib import Path

import nltk
import collections
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from tqdm import tqdm


def _get_word_collection_paths():
    word_collection_txt_paths = []
    for file_name in os.listdir("./temp/word_collection"):
        if not file_name.endswith(".txt"):
            continue
        file_path = os.path.join("./temp/word_collection", file_name)
        word_collection_txt_paths.append(file_path)

    return word_collection_txt_paths


def _tokenize(sentence):
    return word_tokenize(sentence.lower())


def _get_clean_sentence(sentence):
    # Facebook's sometime adds "___ reacted to your message"
    # Since we want our messages, and not facebook generated messages then we can delete those
    if all(x in sentence for x in ['reacted', 'to', 'your', 'message']):
        return ""

    if all(x in sentence for x in ['set', 'the', 'emoji', 'to']):
        return ""

    if all(x in sentence for x in ['changed', 'the', 'chat', 'theme']):
        return ""

    if all(x in sentence for x in ['named', 'the', 'group']):
        return ""

    sentence = sentence.replace("Ã©", "é")
    sentence = re.sub(r'[ðâï]\W{0,3}', '', sentence)
    return sentence


def _get_clean_tokens(uncleaned_tokens):

    tagged_tokens = nltk.pos_tag(uncleaned_tokens)

    valid_tags = ["NN", "NNS", "NNP", "NNPS", "VB"]

    # Only allow valid tags
    tagged_tokens = [t for t in tagged_tokens if t[1] in valid_tags]

    # Remove non-letter words (@, #, *, )
    tagged_tokens = [t for t in tagged_tokens if re.search('\w', t[0])]

    # Remove links
    links = [".com", ".ca", ".net", ".be"]
    tagged_tokens = [t for t in tagged_tokens if not any(link in t[0] for link in links)]

    # Remove queries and equations lol
    tagged_tokens = [t for t in tagged_tokens if "=" not in t[0]]

    cleaned_tokens = [t[0] for t in tagged_tokens]

    return cleaned_tokens


def _remove_stopwords(tokens):
    stop_words = set(stopwords.words('english'))

    filtered_tokens = []

    for w in tokens:
        if w not in stop_words:
            filtered_tokens.append(w)

    return filtered_tokens


def word_collection_2_frequency(wc_filename=None):
    for word_collection_path in _get_word_collection_paths():
        if wc_filename and wc_filename not in word_collection_path:
            continue
        print("Loading " + word_collection_path + "...")
        token_list = []
        with tqdm(total=os.path.getsize(word_collection_path)) as pbar:
            with open(word_collection_path, 'r', encoding='utf-8') as infile:
                for line in infile:
                    # Removed non-sensible words
                    cleaned_line = _get_clean_sentence(line)
                    # Tokenize each sentence/line
                    uncleaned_tokens = _tokenize(cleaned_line)
                    # Remove Stopwords (The, is, are, a, etc.)
                    uncleaned_tokens = _remove_stopwords(uncleaned_tokens)
                    # Removed non-sensible words
                    final_tokens = _get_clean_tokens(uncleaned_tokens)
                    token_list += final_tokens
                    pbar.update(len(line))

        print("Counting...")

        token_frequency = collections.Counter(token_list)

        print("Printing...")

        Path("./temp/frequency").mkdir(parents=True, exist_ok=True)
        with open(word_collection_path.replace("word_collection", "frequency"), "w", encoding="utf-8") as new_file:
            for key in token_frequency.most_common():
                new_file.write(key[0] + " " + str(key[1]) + "\n")
