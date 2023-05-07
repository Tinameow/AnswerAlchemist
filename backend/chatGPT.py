import os
import openai

# Configure OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_summaried_answers(query, answers, word_limit=200):
  template = """\
Answer the query in {} words in html format with reference to the given answers.
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
  return response['choices']['message']['content']
