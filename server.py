from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "Dont worry is safe !"
# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def create_user():
    if session.get('value_list') is None:
        print("Session is empty")
        session['value_list'] = []
    session['value_list'].append(dict(request.form))
    session.modified = True  # Mark the session as modified
    return redirect('/result')

@app.route('/result')
def result_user():
    return render_template("result.html", value_list = session.get('value_list'))

@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)