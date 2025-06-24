app = (_name_)

client = MongoClient('localhost', 27017)
db = client['portfolio_db']
collection = db['contacts']

@app.route('/')
def index():
    return send_file('contact.html')   
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    collection.insert_one({
        'name': name,
        'email': email,
        'message': message
    })

    return "✅ Thank you! Your message has been received."

if _name_ == '_main_':
    app.run(debug=True)