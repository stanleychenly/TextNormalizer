[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/axpepi8Q)

Files in the repository: 
normalize_text.py - The python program that will you will be executing.
bible.txt - The given txt file that will be normalized. You can import your own txt file if you want to use it.
bible_words_graph.png - A sample bar graph of all the options being used.

How to use: 
In the terminal, run: 
$ python normalize_text.py myfile.txt (<your-options>)

The options you have for customization would be the following: 
--lowercasing - Makes all the words lowercase so that they are not case sensitive.
--stemming - Uses stemming to make group words of the same meaning together.
--lemmatization - Uses lemmatization to make group words of the same meaning together.
--removal_of_stopwords - Removes stopwords as per NLTK standard.
--removal_of_punctuation - Removes punctuation from the text.

An example would be: 
$ python normalize_text.py bible.txt --lowercasing --removal_of_punctuation --lemmatization --stemming --removal_of_stopwords

To set up, simply clone the repository onto your device with the following command in the terminal: 
$ git clone https://github.com/4NL3-Winter-2025/homework-assignment-1-stanleychenly.git

Make sure you have python installed.