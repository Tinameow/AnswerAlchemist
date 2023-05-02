import numpy as np
from collections import Counter
# from nltk.tokenize import word_tokenize
from build_model import readQuestions
from build_model import readAnswers
from build_model import readTags
from gensim.utils import tokenize as tk


def tokenize(original_list):
    # print(original_list)
    res_list = []
    for i in range(len(original_list)):
        sentence = original_list[i]
        words = list(tk(sentence))
        res_list.append(words)
        # print(words)
        # break

    return res_list



class bm25Model:


    def __init__(self, k1=2, k2=1, b=0.5):
        self.k1 = k1
        self.k2 = k2
        self.b = b
        self.f = []
        self.idf = {}

        self.num_of_document = None
        self.avg_doc_len = None

    def input_document(self, documents):
        self.num_of_document = len(documents)
        self.avg_doc_len = sum([len(doc) for doc in documents]) / self.num_of_document

        df = {}
        for document in documents:
            temp = {}
            for word in document:
                if word in temp.keys():
                    temp[word] += 1
                else:
                    temp[word] = 1
            self.f.append(temp)
            for word in temp.keys():
                if word in df.keys():
                    df[word] += 1
                else:
                    df[word] = 1
            for key, value in df.items():
                self.idf[key] = np.log((self.num_of_document - value + 0.5)/(value + 0.5))
        return

    def compute_score(self, index, query):
        score = 0.0
        num_of_word_in_doc = len(self.f[index])
        # print("query:", query)
        qf = Counter(query)
        for word in query:
            if word not in self.f[index]:
                continue
            numerator1 = self.idf[word] * (self.f[index][word] * (self.k1+1))
            denominator1 = self.f[index][word] + self.k1 * (1 - self.b + self.b * num_of_word_in_doc / self.avg_doc_len)
            numerator2 = qf[word] * (self.k2+1)
            denominator2 = qf[word] + self.k2
            score += (numerator1/denominator1) * (numerator2/denominator2)
        return score

    def get_score_list(self, query):
        score_list = []
        for i in range(self.num_of_document):
            score_list.append(self.compute_score(i, query))

        return score_list

def query(query):
    # TODO
    query = query.strip().split()

    filepath_Q = 'data/Questions.csv'
    filepath_A = 'data/Answers.csv'
    filepath_T = 'data/Tags.csv'

    my_dict = {}

    readQuestions(filepath_Q, my_dict)
    readAnswers(filepath_A, my_dict)
    readTags(filepath_T, my_dict)

    key_list = []
    title_list = []
    for key in list(my_dict.keys()):
        title = my_dict[key].title
        title_list.append(title)
        key_list.append(key)

    title_list_after_tok = tokenize(title_list)

    my_model = bm25Model()
    my_model.input_document(title_list_after_tok[0:10])
    # print(my_model.idf)
    score_list = my_model.get_score_list(query)

    # print(score_list[0:10])

    combined_list = [(k, s) for k, s in zip(key_list, score_list) if s > 0]
    # combined_list = list(zip(key_list, score_list))
    sorted_combined_list = sorted(combined_list, reverse=True, key=lambda x: x[1])
    sorted_key_list = [x[0] for x in sorted_combined_list]
    # print(sorted_key_list[0:10])

    return sorted_key_list, my_dict

if __name__ == '__main__':

    filepath_Q = 'data/Questions.csv'
    filepath_A = 'data/Answers.csv'
    filepath_T = 'data/Tags.csv'

    my_dict = {}
    # my_list = []

    readQuestions(filepath_Q, my_dict)
    readAnswers(filepath_A, my_dict)
    readTags(filepath_T, my_dict)


    # print(len(list(my_dict.keys())))
    key_list = []
    title_list = []
    for key in list(my_dict.keys()):
        title = my_dict[key].title
        title_list.append(title)
        key_list.append(key)
    # print(title_list)

    title_list_after_tok = tokenize(title_list)
    # print(len(title_list_after_tok))
    # print(title_list_after_tok[0])
    # print(title_list_after_tok[1])
    # print(title_list_after_tok[2])

    query = ['Good']
    # q = "one word".strip().split()
    # print(q)
    # query = tokenize(q)
    
    my_model = bm25Model()
    my_model.input_document(title_list_after_tok[0:10])
    # print(my_model.idf)
    score_list = my_model.get_score_list(query)

    print(score_list[0:10])

    combined_list = list(zip(key_list, score_list))
    sorted_combined_list = sorted(combined_list, reverse=True,  key=lambda x: x[1])
    sorted_key_list = [x[0] for x in sorted_combined_list]
    print(sorted_key_list[0:10])