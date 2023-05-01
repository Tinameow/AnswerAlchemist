from flask import Flask, jsonify
from backend import util as helper

# Initializing flask app
app = Flask(__name__)

# Route for seeing a data
@app.route('/filter')
def get_filter():
    items = helper.filter_ranked_answers()
    return jsonify(items)
  
# Running app
if __name__ == '__main__':
    app.run(debug=True)