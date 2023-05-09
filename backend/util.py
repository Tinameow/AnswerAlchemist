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

def get_dict_details(ques_id):
    cur=conn.cursor()
    query = 'select Questions.Id, Questions.Title, Questions.Body as QBody, Answers.Body as ABody, Answers.Score, Tags.Tag from Answers join Questions on Answers.ParentId = Questions.Id join Tags on Tags.Id = Questions.Id where Questions.Id = {} order by Answers.Score desc;'.format(ques_id)
    cur.execute(query)
    details = cur.fetchall()
    tagList = []
    for entry in details:
        tagList.append(entry[5])
    # print(details)
    return details[0], list(set(tagList))

def get_question(ques_id):
    cur=conn.cursor()
    query = 'select Questions.Id, Questions.Title, Questions.Body as QBody, Answers.Body as ABody, Answers.Score, Tags.Tag, Questions.CreationDate from Answers join Questions on Answers.ParentId = Questions.Id join Tags on Tags.Id = Questions.Id where Questions.Id = {} order by Answers.Score desc;'.format(ques_id)
    cur.execute(query)
    details = cur.fetchall()
    tagList = []
    ansList = []
    for entry in details:
        tagList.append(entry[5])
        ansList.append(entry[3])
    # print(details)
    return details[0], list(set(tagList)), list(set(ansList))
'''
first = rankingList[0]
answer = first.body  # top answer of the input query
title = first.title # question of the top answer
tags = first.tags # tags of top answer
'''
def get_ranked_answers(query_input: str):
    sorted_key_list, question_dict = query(query_input)
    # print(sorted_key_list)
    results = []
    ret_tags = set()
    for i in sorted_key_list:
        details, tags = get_dict_details(i)
        # print(tags)
        results.append(
            {
            "id": i,
            "question": {"title" : details[1],
                        "description" : details[2]
                      },
            "answer": details[3],
            "tags": tags,
            "created": details[4]
            }
        )
        for tag in tags:
            ret_tags.add(tag)

    return results, sorted(list(ret_tags))

def get_ranked_answers_list(id):
    details, tagList, ansList = get_question(id)
    result = {}
    result["id"] = id
    result["question"] = {
        "title": details[1],
        "description": details[2],
        "tags": tagList,
        "created": details[6]
    }
    result["answers"] = ansList
    
    return result
# def get_ranked_answers(query_input: str):
#     sorted_key_list, question_dict = query(query_input)
#     results = []
#     tags = set()
#     for i in sorted_key_list:
#         question = question_dict[i]
#         results.append(
#             {
#             "id": i,
#             "question": {"title" : question.title,
#                         "description" : question.body
#                       },
#             "answer": question.answer,
#             "tags": question.tags,
#             "created": question.creationDate
#             }
#         )
#         for tag in question.tags:
#             tags.add(tag)
#     return results, sorted(list(tags))

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


