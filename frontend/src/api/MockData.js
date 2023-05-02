const mock_results = [
  {
    "id": 1,
    "question": {"title" : "Question title",
                "description" : "Question description"
              },
    "answer": "A answer to the question",
    "tags": ["Python", "Tuple"],
    "created": Date.now()
  },
  {
    "id": 2,
    "question": {"title" : "Question title",
                "description" : "Question description"
              },
    "answer": "A answer to the question",
    "tags": ["Python", "List"],
    "created": Date.now()
  }
]

const mock_tags = ["Python", "Tuple", "List"];

export {mock_results, mock_tags};