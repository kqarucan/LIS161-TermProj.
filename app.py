from flask import Flask, render_template, request, redirect, url_for
from data import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/members/<bang_mem>')
def members(bang_mem):
    membio_list = read_mems_by_mem_type(bang_mem)
    print(membio_list)
    return render_template("members.html",bang_mem=bang_mem, membio=membio_list)
   
    
@app.route('/members/<int:bangmem_id>')
def members_id(bangmem_id):
    bio = read_bangmems_by_bangmem_id(bangmem_id)
    return render_template("bio.html",bio=bio)
#okay so ayos ko na tong upper part, ayusin ko na muna yung nasa
#data.py na part

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/processed', methods=['POST'])
def processing():
    mem_data = {
        "bang_mem": request.form['bang_mem'],
        "fname": request.form['bang_fname'],
        "sname": request.form['bang_sname'],
        "bdate": request.form['bang_bdate'],
        "pbirth": request.form['bang_pbirth'],
        "position": request.form['bang_position'],
        "picurl": request.form['bang_picurl'],
        "line": request.form['bang_line']
    }
    insert_mem(mem_data)
    return redirect(url_for('members', bang_mem=request.form['bang_mem']))
#ina-update pa yung SQL KAYA MEDJ MAHIRAP PA AYUSIN TO

@app.route('/modify', methods=['POST'])
def modify():
    # 1. identify whether user clicked edit or delete
       # if edit, then do this:
    if request.form["modify"] == "edit":
        # retrieve record using id
        bangmem_id = request.form["bangmem_id"] 
        bio = read_bangmems_by_bangmem_id(bangmem_id)
        # update record with new data
        return render_template('update.html', bio=bio)
    # if delete, then do this
    elif request.form["modify"] == "delete":
        # retrieve record using id
        # delete the record
        # redirect user to pet list by pet type
        bangmem_id = request.form["bangmem_id"]
        bio = read_bangmems_by_bangmem_id(bangmem_id)
        delete_mem(bangmem_id)
        return redirect(url_for("members", bang_mem=bio["line"]))

@app.route('/update', methods=['POST'])
def update():
    mem_data = {
        "bangmem_id" : request.form["bangmem_id"],
        "bang_mem": request.form['bang_mem'],
        "fname": request.form['bang_fname'],
        "sname": request.form['bang_sname'],
        "bdate": request.form['bang_bdate'],
        "pbirth": request.form['bang_pbirth'],
        "position": request.form['bang_position'],
        "picurl": request.form['bang_picurl'],
        "line": request.form['bang_line']
    }
    update_mem(mem_data)
    return redirect(url_for('members_id',bangmem_id = request.form['bangmem_id']))

if __name__ == "__main__":
    app.run(debug=True)