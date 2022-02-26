from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
from pymongo import MongoClient
client = MongoClient('mongodb+srv://Seungo:Tulip@cluster0.wfmfn.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
   return render_template('index.html')

@app.route("/homework", methods=["POST"])
def homework_post():
    nickName_receive = request.form['nickName_give']
    comment_receive = request.form['comment_give']
    doc = {
        'nickName': nickName_receive,
        'comment': comment_receive
    }
    db.comment.insert_one(doc)
    return jsonify({'msg': ' 응원이 성공적으로 전달되었습니다 ! '})

@app.route("/homework", methods=["GET"])
def homework_get():
    comment_list = list(db.comment.find({}, {'_id': False}))
    return jsonify({'comments': comment_list})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)
