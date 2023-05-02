from flask import Flask, jsonify, request
import util as helper

# Initializing flask app
app = Flask(__name__)

# Route for seeing a data
@app.route('/filter')
def get_filter():
    data = request.get_json()
    tag = data['tag']
    items = helper.filter_ranked_answers(tag)
    return jsonify(items)

@app.route('/search')
def search():
    data = request.get_json()
    input = data['input']
    items = helper.get_ranked_answers(input)
    return jsonify(items)
  
# Running app
if __name__ == '__main__':
    app.run(debug=True)