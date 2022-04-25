from flask import Flask, render_template
from controllers.categories_controllers import categories_bp
from controllers.merchants_controllers import merchants_bp
from controllers.expenses_controller import expenses_bp
from controllers.budgets_controllers import budgets_bp

app = Flask(__name__)

app.register_blueprint(categories_bp)
app.register_blueprint(merchants_bp)
app.register_blueprint(expenses_bp)
app.register_blueprint(budgets_bp)

@app.route("/")
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()