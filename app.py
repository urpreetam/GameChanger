from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game/<int:box_id>')
def game(box_id):
    # You can pass the box_id to the template to customize the content
    return render_template('game.html', box_id=box_id)

if __name__ == '__main__':
    app.run(debug=True)
