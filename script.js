async function fetchExpenses() {
    const response = await fetch('http://127.0.0.1:5000/expenses');
    const expenses = await response.json();
    const expenseList = document.getElementById('expenseList');
    expenseList.innerHTML = '';
    expenses.forEach(expense => {
        const li = document.createElement('li');
        li.innerHTML = `${expense.description} - $${expense.amount} on ${expense.date} 
        <button onclick="deleteExpense(${expense.id})">Delete</button>`;
        expenseList.appendChild(li);
    });
}

async function addExpense() {
    const description = document.getElementById('description').value;
    const amount = document.getElementById('amount').value;
    const date = document.getElementById('date').value;

    const response = await fetch('http://127.0.0.1:5000/add_expense', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            description: description,
            amount: amount,
            date: date
        })
    });

    if (response.ok) {
        fetchExpenses();
    }
}

async function deleteExpense(id) {
    const response = await fetch(`http://127.0.0.1:5000/expense/${id}`, {
        method: 'DELETE'
    });

    if (response.ok) {
        fetchExpenses();
    }
}

fetchExpenses();
