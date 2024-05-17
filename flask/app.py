from flask import Flask, request, render_template
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB configuration
mongo_uri = "mongodb://<your-mongodb-url>:27017/"
client = MongoClient(mongo_uri)
db = client['user_database']
collection = db['user_details']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    age = request.form.get('age')

    if name and email and age:
        user = {'name': name, 'email': email, 'age': age}
        collection.insert_one(user)
        return 'User details submitted successfully!'
    else:
        return 'Please provide all the details!', 400

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=5000)
