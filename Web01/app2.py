from flask import Flask, rander_template
app = Flask(__name__)


@app.route('/') # tao duong dan
def index():  # thuoc tinh duoc chay
    posts = [
    {
        "title": "Thơ con cóc",
        "content": "Ahihi",
        "author": "Tuấn Anh",
        "gender": "1",
    },
    {
        "title": "Thơ củ lạc",
        "content": "Lạy chúa trên cao turndown 4 what?",
        "author": "Nhật Minh",
        "gender": "1",
    },
    {
        "title": "Thơ con cóc",
        "content": "Sầm Sơn sóng đánh dập dồn Chị em phụ nữ",
        "author": "Quang Dũng",
        "gender": "1",
    },
    ]

    return render_template("index.html", port=port)

@app.route('/c4e')
def sayhi():
    return "Hi C4E 17"

@app.route('/sauhi<name>/<age>/')
def Sayhello(name,age):
    return "Hi {0}, you are {1} yr old".format(name,age)

@app.route('/sum/<int:a>/<int:b>')
def calc(a,b):
    print(sum)
    return str(a + b)

if __name__ == '__main__':
    app.run(debug=True)
