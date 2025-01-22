import re
import nltk
import argparse
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from matplotlib import pyplot as plt

def main(): 
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    parser.add_argument('--lowercasing', action='store_true')
    parser.add_argument('--stemming', action='store_true')
    parser.add_argument('--lemmatization', action='store_true')
    parser.add_argument('--removal_of_stopwords', action='store_true')
    parser.add_argument('--removal_of_punctuation', action='store_true')

    args = parser.parse_args()

    text = read(args.file)
    if args.lowercasing: 
        text = lowercasing(text)
    if args.removal_of_punctuation: 
        text = removal_of_punctuation(text)
    words = text.split()
    if args.stemming:
        words = stemming(words)
    if args.lemmatization: 
        words = lemmatization(words)
    word_list = create_map(words)
    if args.removal_of_stopwords: 
        word_list = removal_of_stopwords(word_list)

    print("List Length: ", len(word_list))
    graph_ranks = []
    graph_numbers = []
    for index in range(25): 
        print(index + 1, ". ", word_list[index][0], " ", word_list[index][1])
    for index in range(-25, 0):
        print(index + len(word_list) + 1, ", ", word_list[index][0], " ", word_list[index][1])

    bar_graph(word_list)

def read(file_name): 
    with open(file_name, "r") as file: 
        text = file.read()
    return text

def create_map(words):
    wordMap = {}
    for word in words:
        wordMap[word] = wordMap.get(word, 0) + 1
    return sorted(wordMap.items(), key=lambda item: item[1], reverse=True)

def lowercasing(text): 
    return text.lower()

def stemming(words):
    ps = PorterStemmer()
    return [ps.stem(word) for word in words]

def lemmatization(words): 
    lemmatizer = WordNetLemmatizer()
    nltk.download('wordnet')
    return [lemmatizer.lemmatize(word) for word in words]

def removal_of_stopwords(word_list):
    nltk.download('stopwords')
    sw = stopwords.words('english')
    return [word for word in word_list if word[0] not in sw]

def removal_of_punctuation(text):
    text = re.sub(r'[,.!?()":;{}]', "", text)
    return text

def bar_graph(word_list):
    positions = range(len(word_list))
    heights = []
    ranks = []
    for index, height in enumerate(word_list): 
        heights.append(height[1])
        ranks.append(index + 1)

    plt.bar(positions, heights)
    plt.xticks(rotation=90)
    plt.yscale('log')

    plt.title("Word Frequency in the Bible")
    plt.xlabel("Rankings")
    plt.ylabel("Occurences")

    plt.show()

if __name__ == "__main__": 
    main()