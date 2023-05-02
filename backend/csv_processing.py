import csv

counter = 0
filepath = 'archive/Tags.csv'
f = open(filepath, 'rt', encoding='ISO-8859-1')
# new_f = open("archive/new_questions.csv", mode="w", newline='', encoding='ISO-8859-1')
# writer = csv.writer(new_f)
# lines = csv.reader(f)
# for line in lines:
#     counter += 1
#     if counter < 12:
#         writer.writerow(line)

ids = ['80','90','120','180','260','330','470','580','650','810']
# new_f = open("archive/new_answers.csv", mode="w", newline='', encoding='ISO-8859-1')
# writer = csv.writer(new_f)
# lines = csv.reader(f)
# header = next(lines)
# writer.writerow(header)
# for line in lines:
#     id = line[-3]
#     if id in ids:
#         writer.writerow(line)

new_f = open("archive/new_tags.csv", mode="w", newline='', encoding='ISO-8859-1')
writer = csv.writer(new_f)
lines = csv.reader(f)
header = next(lines)
writer.writerow(header)
for line in lines:
    id = line[0]
    if id in ids:
        writer.writerow(line)

f.close()
new_f.close()