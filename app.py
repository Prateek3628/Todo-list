from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
db = SQLAlchemy(app)

class todo(db.Model):
    sno = db.Column(db.Integer,primary_key = True)
    title =db.Column(db.String(200),nullable = False)
    desc =db.Column(db.String(500),nullable = False)
    date_created =db.Column(db.DateTime,default = datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"
    
   
@app.route('/',methos=["Post" ])
def hello_world():
    if request.methods=="Post":
        title=request.form['title']
        desc=request.form['desc']

    Todo = todo(tile = "First Todo" desc = "start falsk today")
    db.session.add(Todo)
    db.session.commit()
    allTodo=Todo.query.all()
    print(allTodo);
    return render_template('index.html',allTodo=allTodo)
    # return 'Hello, World!'

@app.route('/show')
def products():
    allTodo=todo.query.all()
    print(allTodo)
    return 'This is products page'
    
@app.route('/update/<int:sno>', method = ['GET','POST'])
def update(sno):
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        Todo=todo.query.filter_by(sno = sno).first()
        todo.title = title
        todo.desc = desc
        db.session.add(todo)
        db.session.commit()
        return redirect("/")

    Todo=todo.query.filter_by(sno = sno).first()
    return render_template('update.html',todo = todo)

@app.route('/delete/<int:sno>')
def delete(sno):
    Todo=todo.query.filter_by(sno = sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/")

if __name__ == '__main__':
    app.run(debug = True)