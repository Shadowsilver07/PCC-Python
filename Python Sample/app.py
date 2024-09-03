from flask import Flask, jsonify

app = Flask(__name__)

# Sample data (you'd normally get this from a database)
users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"}
]

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)