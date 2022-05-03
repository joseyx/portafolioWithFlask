from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')  # default route
def landing_page():
    return render_template('index.html', content='landing')


@app.route('/about')  # about route
def about_page():
    return render_template('about.html', content='about')


@app.route('/contact')  # contact route
def contact_page():
    return render_template('Form.html', content='contact')


if __name__ == '__main__':
    app.run()
