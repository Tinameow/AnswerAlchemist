import csv
import requests

# Set the API endpoints
questions_url = "https://api.stackexchange.com/2.3/questions"
answers_url = "https://api.stackexchange.com/2.3/questions/{question_id}/answers"

# Set the parameters for the API request for questions
questions_params = {
    "site": "stackoverflow",
    "pagesize": 100,  # Number of questions per page
    "page": 1         # Page number
}

# Open the CSV file for writing
with open("stackoverflow.csv", "w", newline="", encoding="utf-8") as csvfile:
    # Create a CSV writer
    csvwriter = csv.writer(csvfile)

    # Write the headers to the CSV file
    csvwriter.writerow(["Question ID", "Title", "Tags", "Answer"])

    # Loop through all the pages of questions
    while True:
        # Make the API request for questions
        response = requests.get(questions_url, params=questions_params)

        # Check if the API request for questions was successful
        if response.status_code != 200:
            print("Error: Failed to retrieve questions")
            break

        # Parse the JSON response and write the questions and answers to the CSV file
        data = response.json()
        for question in data["items"]:
            # Set the parameters for the API request for answers
            # answers_params = {
            #     "site": "stackoverflow",
            #     "pagesize": 100,  # Number of answers per page
            #     "page": 1,        # Page number
            #     "question_id": question["question_id"]
            # }
            # let answers be sorted desc by votes
            answer_params = {
                'site': 'stackoverflow',
                'order': 'desc',
                'sort': 'votes',
                'filter': 'withbody', # Include the body field in the response
                "question_id": question["question_id"]
            }

            # Make the API request for answers
            answer_response = requests.get(answers_url.format(question_id=question["question_id"]), params=answer_params)
            # answer_response = requests.get(answers_url, params=answer_params)

            # Check if the API request for answers was successful
            if answer_response.status_code != 200:
                print("Error: Failed to retrieve answers for question", question["question_id"])
                continue

            # Parse the JSON response and write the question and its answers to the CSV file
            answer_data = response.json()
            # get the top answer
            if answer_data['items']:
                top_answer = answer_data['items'][0]
                # print(f"Top answer: {top_answer['body']}\n")
            else:
                top_answer = "No answers found."
            # for answer in data["items"]:
            #     csvwriter.writerow([question["question_id"], question["title"], ", ".join(question["tags"]), top_answer])
            csvwriter.writerow([question["question_id"], question["title"], ", ".join(question["tags"]), top_answer])

        # Check if there are more pages of questions
        if not data["has_more"]:
            break

        # Increment the page number
        questions_params["page"] += 1
