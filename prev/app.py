from flask import Flask, render_template,g,request
import sqlite3
app = Flask(__name__)
def connect_db():
    sql=sqlite3.connect('/home/vipul/Desktop/Food_tracker/mydatabase.db')
    sql.row_factory=sqlite3.Row
    return sql
def get_db():
    if hasattr(g,'sqlite3'):
        return g.sqlite_db
    else:
        g.sqlite_db=connect_db()
    return g.sqlite_db
@app.teardown_appcontext
def close_db(error):
    if hasattr(g,'sqlite_db'):
        g.sqlite_db.close()
@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        return request.form['']
    return render_template('home.html')

@app.route('/view')
def view():
    return render_template('day.html')

@app.route('/food',methods=['GET','POST']) 
def food():
    db=get_db()
    if request.method=='POST':
        n=request.form.get('food-name')
        pro=int(request.form.get('protein'))
        carbo=int(request.form['carbohydrates'])
        fat=int(request.form['fat'])
        cal=pro*4+carbo*4+fat*9
        db.execute('insert into food(name,protein,carbohydrates,fat,cal) values(?,?,?,?,?)', \
         [n,pro,carbo,fat,cal])
        db.commit()
    cur=db.execute('select name,protein,carbohydrates,fat,cal from food')
    result=cur.fetchall()
    return render_template('add_food.html',res=result)

if __name__ == '__main__':
    app.run(debug=True)