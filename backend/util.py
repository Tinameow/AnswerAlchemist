from ranking import rankingList
from ranking import rawList

'''
first = rankingList[0]
answer = first.body  # top answer of the input query
title = first.title # question of the top answer
tags = first.tags # tags of top answer
'''

# if ranked list, filter the ranked list, otherwise, filter the original list
def filter_ranked_answers(tag: str):
    filtered_list = []
    if rankingList:
        row_list = rankingList
    else:
        row_list = rawList
    for row in row_list:
        tag_list = row.tags
        if tag in tag_list:
            item = {
                "title": row.title,
                "questionBody": row.body,
                "answer": row.answers,
                "tags": tag_list
                }
            filtered_list.append(item)
    return filtered_list