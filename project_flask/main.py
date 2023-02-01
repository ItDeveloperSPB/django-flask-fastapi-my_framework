from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
async def template_():
    return render_template('template.html',
                           title="Основной сайт",
                           object_list=[1, 23, 4, 5, 6])


if __name__ == '__main__':
    app.run(debug=True, port=5001)
