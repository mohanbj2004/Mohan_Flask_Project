from flask import Flask, render_template, request, redirect, url_for
import csv
import os
from datetime import datetime

app = Flask(__name__)
FILENAME = 'expenses.csv'

def initialize_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Date', 'Category', 'Amount', 'Note'])

@app.route('/')
def index():
    initialize_file()
    expenses = []
    with open(FILENAME, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            expenses.append(row)
    return render_template('index.html', expenses=expenses)

@app.route('/add', methods=['POST'])
def add_expense():
    date = request.form['date']
    category = request.form['category']
    amount = request.form['amount']
    note = request.form['note']

    with open(FILENAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, note])

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
