import imp
from flask import Flask, render_template
from controllers.categories_controllers import categories_bp

app = Flask(__name__)

app.register_blueprint(categories_bp)

@app.route("/")
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()