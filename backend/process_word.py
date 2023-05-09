import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

nltk.download('stopwords')
nltk.download('wordnet')

# 这里的函数输入为list of words对接token之后的列表，输出为经过处理之后的列表

def process_list_of_word(tokens):

    # 全变成小写，如果有更好的方法可以替换
    tokens = [token.lower() for token in tokens]

    # 去掉标点符号，以及一些奇怪的符号，例如<>这样的
    tokens = [token for token in tokens if token not in string.punctuation]

    # 去掉stop words
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]

    # 提取stem，也就是词干
    stemmer = PorterStemmer()
    tokens = [stemmer.stem(token) for token in tokens]

    # lemmatization，词型还原
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]

    return tokens


