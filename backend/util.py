from ranking import rankingList
import csv

'''
first = rankingList[0]
answer = first.body  # top answer of the input query
title = first.title # question of the top answer
tags = first.tags # tags of top answer
'''

def read_from_csv():
    # Open the CSV file in read mode
    ranked_list = []
    with open('train.csv', 'r') as file:

        # Create a reader object
        reader = csv.reader(file)

        # Iterate over each row in the CSV file
        for row in reader:

            # Access the data in each column of the row
            title = row[1]
            body = row[2]
            tags = row[3]

            # Do something with the data
            # print(title, body, tags)
            # convert tags from string to list
            tag_list = tags.split("<")[1:]
            tag_list = [elem[:-1] for elem in tag_list]
            tmp_tuple = (title, body, tag_list)
            ranked_list.append(tmp_tuple)
    return ranked_list



# if ranked list, filter the ranked list, otherwise, filter the original list
def filter_ranked_answers(tag: str):
    filtered_list = []
    if rankingList:
        ranked_list = rankingList
        for row in ranked_list:
            tmp_tags = row.tags
            # if not convert tags to list
            tag_list = tmp_tags.split("<")[1:]
            tag_list = [elem[:-1] for elem in tag_list]
            if tag in tag_list:
                item = {
                    "title": row.title,
                    "answer": row.body,
                    "tags": tag_list
                    }
                filtered_list.append(item)
    else:
        ranked_list = read_from_csv()
        for row in ranked_list:
            tmp_tags = row[2]
            if tag in tmp_tags:
                item = {
                    "title": row[0],
                    "answer": row[1],
                    "tags": tmp_tags
                    }
                filtered_list.append(item)
    return filtered_list

