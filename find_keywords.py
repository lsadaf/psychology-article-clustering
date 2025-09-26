from hazm import *
import csv
import numpy as np
import scipy.io as sio
import matplotlib.pyplot as plt
import pandas as pd
from scipy import io


from sklearn.feature_extraction.text import TfidfVectorizer
# Initialize NLP tools
# normalizer = Normalizer()
# tokenizer = WordTokenizer()
# lemmatizer = Lemmatizer()
posTagger = POSTagger(model='pos_tagger.model')




# Tokenize using hazm

normalizer = Normalizer()
tokenizer = WordTokenizer()
lemmatizer = Lemmatizer()
# posTagger = POSTagger(model='resources/pos_tagger.model')
forbidden_word_types = ['PUNCT', 'CCONJ', 'VERB', 'ADP', 'SCONJ', 'DET', 'NUM', 'PRON']


def tokenize_news(news_content):
    persian_alphabet = ['ا' , 'آ' ,'ب' , 'پ' , 'ت' , 'ث' , 'ج' , 'چ' , 'ح' , 'خ' ,'د','ذ', 'ر' , 'ز' ,'ژ' ,
                         'س' ,'ش' ,'ص' ,'ض' ,'ط' ,'ظ' ,'ع' ,'غ' ,'ف'
                        ,'ق','ک','گ','ل','م','ن','و','ه','ی']
    normalized_news = normalizer.normalize(news_content)
    normalized_news = normalizer.remove_specials_chars(normalized_news)
    tokenized_news = tokenizer.tokenize(normalized_news)
    tagged_tokenized_news = posTagger.tag(tokens=tokenized_news)
    clean_tagged_tokenized_news = []
    for word in tagged_tokenized_news:
        if all(word_type not in word[1] for word_type in forbidden_word_types) and ('!' not in word[0]) and (
                '?' not in word[0]
                and all(c in persian_alphabet for c in word[0])
                #and "\u" not in word[0]
                and word[0] != "هدف"
                and word[0] != "پژوهش"
                and word[0] != "بررسی"
                and word[0] != "حاضر"
                and ")" not in word[0]
                and "(" not in word[0]
                and "]" not in word[0]
                and "[" not in word[0]

        ):
            lemmatized_word = lemmatizer.lemmatize(word[0])
            clean_tagged_tokenized_news.append(lemmatized_word)


    # Log : Cleaned tokenized news
    print(clean_tagged_tokenized_news)
    return clean_tagged_tokenized_news


def process_content(content):
    persian_alphabet = ['ا' , 'آ' ,'ب' , 'پ' , 'ت' , 'ث' , 'ج' , 'چ' , 'ح' , 'خ' ,'د','ذ', 'ر' , 'ز' ,'ژ' ,
                         'س' ,'ش' ,'ص' ,'ض' ,'ط' ,'ظ' ,'ع' ,'غ' ,'ف'
                        ,'ق','ک','گ','ل','م','ن','و','ه','ی']
    all_nums = ['0' , '1' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9']
    content = normalizer.normalize(content)
    tokenized_content = tokenizer.tokenize(content)
    tagged = posTagger.tag(tokens=tokenized_content)
    new_listof_tokenized = []

    for tok in tagged:
        if (
            all(c in persian_alphabet for c in tok[0])
            and all (x not in all_nums for x in tok[0])
            and tok[1] != "NUM,EZ"
            and tok[1] != "NUM"
            and tok[1] != "ADP"
            and tok[1] != "CCONJ"
            and tok[1] != "PUNCT"
            and tok[1] != "VERB"
            and tok[1] != "PUNCT"
            and tok[1] != "VERB"
            and tok[1] != "SCONJ"
            and tok[1] != "DET"
            and tok[1] != "PRON"
            and tok[0] != "هدف"
            and tok[0] != "پژوهش"
            and tok[0] != "بررسی"
            and tok[0] != "حاضر"
            and tok[0] != ")"
            and tok[0] != "("

        ):
            lemmatized_content = lemmatizer.lemmatize(tok[0])
            new_listof_tokenized.append(lemmatized_content)

    return ' '.join(new_listof_tokenized)


contents = []
keywords = []
with open('all_articles300.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        contents.append(row[1] + row[2])
        # contents.append(row[2])
        keywords.append(row[2])

# content, kw = (contents, keywords)[0]
# test=tokenize_news(content).append(kw)

# total_documents = [tokenize_news(content).append(kw) for (content, kw) in zip(contents, keywords)]
total_documents = [tokenize_news(content) for content in contents]

print(total_documents)
print(len(total_documents))






combined_data = []
with open('all_articles300.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row, content in zip(reader, total_documents):
        combined_data.append([row[0], content])


with open('D:/Data Mining/project/all_keywords300.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['URL', 'Keywords'])
    writer.writerows(combined_data)
