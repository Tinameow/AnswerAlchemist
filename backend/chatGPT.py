import os
import openai
from config import OPENAI_API_KEY

# Configure OpenAI API key
# openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

def get_summaried_answers(query, answers, word_limit=100):
  template = """\
Answer the query in {} words in well-format html with reference to the given answers.
Query: {}
{}
"""
  answers = "".join([f"Answer {answer['id']}: {answer['answer']}\n" for answer in answers])
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
          {"role": "user", 
           "content": template.format(word_limit, query, answers)}
      ]
  )
  print(response)
  return response['choices'][0]['message']['content']

if __name__ == "__main__":
  mock_results = [
        {
            "id": 1,
            "question": {"title" : "Question title",
                        "description" : "Question description"
                      },
            "answer": "A answer to the question",
            "tags": ["Python", "Tuple"]
        },
        {
            "id": 2,
            "question": {"title" : "Question title",
                        "description" : "Question description"
                      },
            "answer": "A answer to the question",
            "tags": ["Python", "List"]
        }
    ]
  query = "give an answer to the question"
