import requests

# Set the API endpoint URL
url = 'https://api.stackexchange.com/2.3/questions'

# Set the query parameters
params = {
    'site': 'stackoverflow',
    'order': 'desc',
    'sort': 'votes',
    'tagged': 'python',
    'filter': 'withbody' # Include the body field in the response
}

# Make a GET request to the API
response = requests.get(url, params=params)

# Extract the JSON data from the response
data = response.json()

# Loop through the questions and print the title and body
for question in data['items']:
    print(f"Title: {question['title']}")
    print(f"Question: {question['body']}\n")

    # Get the answers to the question
    answer_url = f"https://api.stackexchange.com/2.3/questions/{question['question_id']}/answers"
    answer_params = {
        'site': 'stackoverflow',
        'order': 'desc',
        'sort': 'votes',
        'filter': 'withbody' # Include the body field in the response
    }
    answer_response = requests.get(answer_url, params=answer_params)
    answer_data = answer_response.json()

    # Print the top answer
    if answer_data['items']:
        top_answer = answer_data['items'][0]
        print(f"Top answer: {top_answer['body']}\n")
    else:
        print("No answers found.\n")
