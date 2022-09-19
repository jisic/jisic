from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.n6v3trp.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
    return render_template('attendaccount.html')

@app.route("/toyproject", methods=["POST"])
def toyprojects_post():
    name_receive = request.form['name_give']
    id_receive = request.form['id_give']
    password_receive = request.form['password_give']
    phone_receive = request.form['phone_give']
    email_receive = request.form['email_give']

    doc = {
        'name': name_receive,
        'id': id_receive,
        'password': password_receive,
        'phone': phone_receive,
        'email': email_receive
    }
    db.toyprojects.insert_one(doc)

    return jsonify({'msg':'가입이 완료되었습니다! 재로그인 해주세요.'})

@app.route("/toyproject", methods=["GET"])
def toyprojects_get():
    toyproject_list = list(db.toyprojects.find({}, {'_id': False}))
    return jsonify({'toyprojects': toyproject_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)