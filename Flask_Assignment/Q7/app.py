from flask import Flask, render_template, request, url_for
import sqlite3 as sql

app = Flask('__name__')


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/enternew')
def new_student():
    return render_template('student.html')

@app.route('/addrecord', methods=['POST', 'GET'])
def addrecord():
    if request.method == 'POST':
        try:
            name = request.form['nm']
            ID = request.form['id']
            subject = request.form['sub']

            with sql.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO students (NAME, ID, SUBJECT) VALUES (?,?,?)", (name, ID, subject))
                con.commit()
                msg = "Record sucessfully added"

        except:
            con.rollback()
            msg = "error in insert"

        finally:
            return render_template("result.html", msg=msg)
            con.close()

@app.route('/list')
def list():
    con = sql.connect("database.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from students")
    rows = cur.fetchall()
    return render_template('list.html', rows = rows)


@app.route('/delete')
def delete():
    return render_template('delete.html')

@app.route('/delete_record', methods=['POST'])
def delete_record():
    if request.method == 'POST':
        try:
            student_id = request.form['id']

            with sql.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("DELETE FROM students WHERE ID = ?", (student_id,))
                con.commit()
                msg = f"Record with ID {student_id} deleted successfully"

        except:
            con.rollback()
            msg = "Error in delete operation"

        finally:
            return render_template("result.html", msg=msg)
            con.close()



if __name__ == '__main__':
    app.run(debug = True)