from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses.db'
db = SQLAlchemy(app)

# Model for Expense
class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.String(10), nullable=False)

# Create the database
with app.app_context():
    db.create_all()

@app.route('/add_expense', methods=['POST'])
def add_expense():
    data = request.get_json()
    new_expense = Expense(description=data['description'], amount=data['amount'], date=data['date'])
    db.session.add(new_expense)
    db.session.commit()
    return jsonify({'message': 'Expense added successfully'}), 201

@app.route('/expenses', methods=['GET'])
def get_expenses():
    expenses = Expense.query.all()
    expenses_list = [{
        'id': exp.id,
        'description': exp.description,
        'amount': exp.amount,
        'date': exp.date
    } for exp in expenses]
    return jsonify(expenses_list), 200

@app.route('/expense/<int:id>', methods=['DELETE'])
def delete_expense(id):
    expense = Expense.query.get_or_404(id)
    db.session.delete(expense)
    db.session.commit()
    return jsonify({'message': 'Expense deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
