from flask import Flask, jsonify, request
from flask_cors import CORS
import util 
from datetime import datetime

# Initializing flask app
app = Flask(__name__)
cors = CORS(app)

# Route for seeing a data
@app.route('/filter')
def get_filter():
    data = request.get_json()
    tag = data['tag']
    items = util.filter_ranked_answers(tag)
    return jsonify(items)

@app.route('/search', methods=['GET'])
def search():
    keywords = request.args.get('keywords', None)
    limit = int(request.args.get('limit', 100))
    offset = int(request.args.get('offset', 0))

    # result = util.get_ranked_answers(keywords)
    # tags = []

    # Perform search based on keywords, limit, and offset
    # Return mock_results for now
    mock_results = [
        {
            "id": 1,
            "question": {"title" : "Question title",
                        "description" : "Question description"
                      },
            "answer": "A answer to the question",
            "tags": ["Python", "Tuple"],
            "created": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        },
        {
            "id": 2,
            "question": {"title" : "Question title",
                        "description" : "Question description"
                      },
            "answer": "A answer to the question",
            "tags": ["Python", "List"],
            "created": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
    ]
    mock_tags = ["Python", "Tuple", "List"]
    return jsonify({"data": {"results": mock_results, "tags": mock_tags}})

  
# Running app
if __name__ == '__main__':
    app.run(debug=True)