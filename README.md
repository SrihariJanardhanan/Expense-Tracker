# Expense Tracker

This is a simple Expense Tracker app built using Flask for the backend and HTML, CSS, and JavaScript for the frontend.

## Features
- Add an expense (description, amount, date)
- View all expenses
- Delete an expense

## Running the project
1. Clone this repository.
2. Install Flask: `pip install Flask`.
3. Run the backend server: `python app.py`.
4. Open `index.html` in a browser.

## Endpoints
- `/add_expense` (POST) - Add a new expense
- `/expenses` (GET) - Get all expenses
- `/expense/<id>` (DELETE) - Delete an expense
