"""
Counter API Implementation
"""
from flask import Flask, jsonify
from . import status    

app = Flask(__name__)

COUNTERS = {}

@app.route('/counters/<name>', methods=['POST'])
def create_counter(name):
    """Create a counter"""
    if counter_exists(name):
        return jsonify({"error": f"Counter {name} already exists"}), status.HTTP_409_CONFLICT
    COUNTERS[name] = 0
    return jsonify({name: COUNTERS[name]}), status.HTTP_201_CREATED

def counter_exists(name):
  """Check if counter exists"""
  return name in COUNTERS

@app.route('/counters', methods=['GET'])
def list_all_counters():
    #lists all the counters
    return jsonify(COUNTERS), status.HTTP_200_OK

# Write code to make test pass - Brian
@app.route('/counters/<name>', methods=['GET'])
def read_counter(name):
    """Read a counter"""
    # Check if the counter exists in our dictionary
    if name in COUNTERS:
        return jsonify({name: COUNTERS[name]}), status.HTTP_200_OK
    
    # If not found, return 404
    return jsonify({"error": f"Counter {name} does not exist"}), status.HTTP_404_NOT_FOUND
