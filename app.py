from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def landing_page():
    return render_template('index.html', content='test')


@app.route('/about')
def about_page():
    return render_template('about.html', content='test')


if __name__ == '__main__':
    app.run()
