from flask import render_template,redirect,request
from flask_app import app
from flask_app.models import dojo, ninja

@app.route('/ninjas')
def ninjas():
    
    return render_template('ninjas.html', dojos=dojo.Dojo.get_all())

@app.route('/create/ninja', methods=['POST'])
def create_ninja():
    data = {
        "dojo_id":request.form['dojo_id'],
        "first_name":request.form['first_name'],
        "last_name":request.form['last_name'],
        "age":request.form['age']
    }
    ninja.Ninja.save(data)
    return redirect(f'/dojo/{request.form["dojo_id"]}')

@app.route('/ninja/edit/<int:id>')
def edit(id):
    data = {
        'id': id
    }
    return render_template('edit_ninja.html', title='edit', ninja=ninja.Ninja.get_one(data))

@app.route('/ninja/print/<int:id>')
def print(id):
    data = {
        'id': id
    }
    return render_template('print_ninja.html', title='print', ninja=ninja.Ninja.get_one(data))


@app.route('/ninja/update', methods=['POST'])
def update():
    data = {
        "id":request.form['id'],
        "first_name":request.form['first_name'],
        "last_name":request.form['last_name'],
        "age":request.form['age']
    }
    ninja.Ninja.update(data)
    return redirect(f'/ninja/print/{request.form["id"]}')

@app.route('/ninja/delete/<int:id>/<int:dojo_id>')
def delete(id,dojo_id):
    data = {
        'id': id
    }
    ninja.Ninja.delete(data)
    return redirect(f'/dojo/{dojo_id}')
