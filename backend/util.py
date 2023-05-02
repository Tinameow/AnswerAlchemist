from BM25 import query

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


    