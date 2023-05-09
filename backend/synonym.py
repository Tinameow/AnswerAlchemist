import nltk
nltk.download('wordnet')

from nltk.corpus import wordnet as wn

def find_synonyms(word, pos=None):
    synsets = wn.synsets(word, pos=pos)
    synonyms = set()
    for synset in synsets:
        for lemma in synset.lemmas():
            synonyms.add(lemma.name())
    return list(synonyms)

# 直接调用这个函数，把word1和word2传进去，return一个bool
# 这里的pos是part of speech，词性的意思，可以不传
def is_synonym(word1, word2, pos=None):
    synsets1 = wn.synsets(word1, pos=pos)
    synsets2 = wn.synsets(word2, pos=pos)
    common_synsets = set(synsets1).intersection(synsets2)
    return len(common_synsets) > 0




# 下面这些是基于gensim实现的，因为不确定nltk能不能用
# import gensim.downloader as api
#
# def load_word_vectors():
#     model = api.load('word2vec-google-news-300')
#     return model
#
# def find_synonyms(word, model, topn=10):
#     return model.most_similar(positive=[word], topn=topn)
#
# def is_synonym(word1, word2, model, threshold=0.5):
#     similarity = model.similarity(word1, word2)
#     return similarity >= threshold
#
#
# # 直接调用这个函数，把word1和word2传进去，return一个bool
# def check_synonym(word1, word2):
#     model = load_word_vectors()
#     result = is_synonym(word1, word2, model, threshold=0.5)
#     return result