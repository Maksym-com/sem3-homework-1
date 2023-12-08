from flask import Flask, render_template, send_from_directory

app = Flask('oderman', template_folder="templates", static_folder="static")

@app.route('/')
@app.route('/index')
def index_view():
    return render_template("menu.html")

@app.route('/menu')
def serve_static():
    return render_template("menu1.html")


# Якщо є слеш в кінці роута, то буде працювати запит і з роутом і без.
# Якщо слеш не вказувати, то буде працювати тільки без слешу


if __name__ == "__main__":
    # host = 'localhost'
    # port = 5001
    app.run(debug=True)