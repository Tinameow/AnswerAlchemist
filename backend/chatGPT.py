import os
import openai
from config import OPENAI_API_KEY

# Configure OpenAI API key
# openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

def get_summaried_answers(query, answers, word_limit=200):
  template = """\
Answer the query in {} words with bullet points.
If the answers can be the answer for the query, summerize the answers as reference. Otherwise, simply answer the query. Provide an example if nessessary.

Query: {}
Answers:
{}
"""
  answers = "".join([f"Answer {i+1}: {answer['answer']}\n" for i,answer in enumerate(answers)])
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
          {"role": "user", 
           "content": template.format(word_limit, query, answers)}
      ]
  )
  # print(response)
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
