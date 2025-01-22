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
$ git clone https://github.com/stanleychenly/TextNormalizer.git

Make sure you have python installed.
