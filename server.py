from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key ='12345'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/show')
def show():
    return render_template("show.html", name_on_form=session['name'], location_on_form=session['location'], language_on_form=session['location'], comment_on_form=session['comment'])

@app.route('/user', methods=['post'])
def user():
    print(request.form)
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/show')

if __name__ == "__main__":
    app.run(debug=True)