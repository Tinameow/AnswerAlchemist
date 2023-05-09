from BM25 import query
import pymysql
'''
Tables:
    -Questions
    -Answers
    -Tags
Table describe:
Questions(Id(PRIMARY KEY): INT, CreationDate: VAR(255), Score: INT, Title: VAR(255), Body: LONGTEXT)
Answers(Id(PRIMARY KEY): INT, CreationDate: VAR(255), ParentId(FOREIGN KEY): INT, Score: INT, Body: LONGTEXT)
Tags(Id(FOREIGN KEY): INT, Tag: TEXT)
'''
conn = pymysql.connect(
        host= 'database-i-510.chrgejp9gwu0.us-east-1.rds.amazonaws.com', 
        port = 3306,
        user = 'admin', 
        password = '123Qazwsx123!',
        db = 'database510',
        )
'''
#read the data (examples)
def get_details():
    cur=conn.cursor()
    cur.execute("select Questions.Body from Answers join Questions on Answers.ParentId = Questions.Id join Tags on Tags.Id = Questions.Id where Questions.Body LIKE '%SQL%'")
    details = cur.fetchall()
    print(details)
    # return details
'''

'''
first = rankingList[0]
answer = first.body  # top answer of the input query
title = first.title # question of the top answer
tags = first.tags # tags of top answer
'''
def get_ranked_answers(query_input: str):
    sorted_key_list, question_dict = query(query_input)
    results = []
    tags = set()
    for i in sorted_key_list:
        question = question_dict[i]
        results.append(
            {
            "id": i,
            "question": {"title" : question.title,
                        "description" : question.body
                      },
            "answer": question.answer,
            "tags": question.tags,
            "created": question.creationDate
            }
        )
        for tag in question.tags:
            tags.add(tag)
    return results, sorted(list(tags))

# if ranked list, filter the ranked list, otherwise, filter the original list
# def filter_ranked_answers(tag: str):
#     filtered_list = []
#     row_list = []
#     if rankingList:
#         row_list = rankingList(tag)
#     for row in row_list:
#         tag_list = row.tags
#         if tag in tag_list:
#             item = {
#                 "title": row.title,
#                 "questionBody": row.body,
#                 "answer": row.answers,
#                 "tags": tag_list
#                 }
#             filtered_list.append(item)
#     if len(filtered_list) >= 5:
#         return filtered_list[:5]
#     else: 
#         return filtered_list[:len(filtered_list)]


# get_details()