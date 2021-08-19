from flask import Flask, request, redirect, render_template, render_template_string, url_for, session


app = Flask(__name__)
app.secret_key = "marcos"


@app.route('/', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        session['login'] = request.form['login']        
        return redirect(url_for("get_email"))
    return render_template('login.html')

@app.route('/get_email')
def get_email():
    return render_template_string("""
            {% if session['login'] %}
                <h1>Welcome {{ session['login'] }}!</h1>
            {% else %}
                <h1>Welcome! Please enter your email <a href="{{ url_for('set_email') }}">here.</a></h1>
            {% endif %}
        """)

'''
@app.route("/")
def home_page():
    return render_template("index.html")
    
@app.route("/home/")
def animes():
    return render_template("animes.html")
'''


if __name__ == "__main__":
    app.run(debug=True)