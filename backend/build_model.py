import csv
import re


filepath_Q = 'archive/Questions.csv'
filepath_A = 'archive/Answers.csv'
filepath_T = 'archive/Tags.csv'

my_dict = {}
# my_list = []

class Entry():


    def __init__(self, id):

        self.id = id
        self.ownerUserId = None
        self.creationDate = None
        self.closedDate = None
        self.Qscore = None
        self.title = None
        self.body = None
        self.answer = None # string
        self.Ascore = None
        self.tags = []

    def add_info(self, ownerUserId=None, creationDate=None, closedDate=None, score=None, title=None, body=None):

        self.ownerUserId = ownerUserId
        self.creationDate = creationDate
        self.closedDate = closedDate
        self.Qscore = score
        self.title = title
        self.body = body

    def add_answer(self, score, answer):

        if self.Ascore == None or self.Ascore < score:
            self.Ascore = score
            self.answer = answer

    def add_tag(self, tag):
        self.tags.append(tag)


# readfile
def readQuestions(filepath, entry_dict):

    with open(filepath, 'rt', encoding='ISO-8859-1') as f:
        lines =  csv.reader(f)
        header = next(lines) # remove the first row (header)
        for line in lines:
            if line != None:
                id, ownerUserId, creationDate, closedDate, score, title, body = line

                my_entry = Entry(id=id)
                my_entry.add_info(ownerUserId=ownerUserId, creationDate=creationDate, closedDate=closedDate, score=score, title=title, body=body)

                # entry_list.append(my_entry)
                entry_dict[id] = my_entry


def readAnswers(filepath, entry_dict):
    with open(filepath, 'rt', encoding='ISO-8859-1') as f:
        lines =  csv.reader(f)
        header = next(lines)
        for line in lines:
            if line != None:
                parentId, score, answer = line[-3], line[-2], line[-1]
                entry_dict[parentId].add_answer(score, answer)


def readTags(filepath, entry_dict):
    with open(filepath, 'rt', encoding='ISO-8859-1') as f:
        lines = csv.reader(f)
        header = next(lines)
        for line in lines:
            if line != None:
                parentId, tag = line
                entry_dict[parentId].add_tag(tag)


if __name__ == '__main__':
    readQuestions(filepath_Q, my_dict)
    readAnswers(filepath_A, my_dict)
    readTags(filepath_T, my_dict)

    print(len(list(my_dict.keys())))
    # print(my_dict['80'].title)
    # print(my_dict['80'].answer)
    # print(my_dict['80'].Ascore)
