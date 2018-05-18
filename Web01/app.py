from flask import Flask, render_template
app = Flask(__name__)


@app.route('/') # tạo ra đường dẫn
def index():    # thuộc tinh được chạy
    posts = [
        {
            "title" : "Thơ con cóc",
            "content" : "Ahihi",
            "author" : "Tuấn Anh",
            "gender" :1,
        },
        {
            "title" : "Thơ củ lạc",
            "content" : "Lạy chú trên cao turndown 4 what?",
            "author" : "Nhật Minh",
            "gender": 1,
        },
        {
            "title" : "Thơ con cóc",
            "content" : "Sầm Sơn sóng đánh dập dồn Chị em phụ nữ ",
            "author" : "Quang Dũng"
            "gender": 1,
        }
    ]


    return render_template("index.html", posts=posts)

@app.route('/c4e')
def sayhi():
    return "Hi C4E 17"

@app.route('/sayhi/<name>/<age>') # request parameter dung de thay doi noi dung cho mot trang
def Sayhello(name, age):
    return "Hi {0}, you are {1} yr old".format(name, age)

@app.route('/sum/<int:a>/<int:b>') # route Luon tr ra string
def calc(a,b):
    print(sum)
    return str(a + b) # return luon tra ve chu, nen boc so tra ve chu

if __name__ == '__main__':
  app.run(debug=True)
