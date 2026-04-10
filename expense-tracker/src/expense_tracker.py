#!/usr/bin/env python3
"""
Expense Tracker CLI Application

A simple command-line tool to track personal expenses.
Helps users manage their finances by recording, viewing, and summarizing expenses.
"""

import argparse
import json
import os
from datetime import datetime

DATA_FILE = 'expenses.json'


def load_expenses():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []


def save_expenses(expenses):
    with open(DATA_FILE, 'w') as f:
        json.dump(expenses, f, indent=4)


def add_expense(amount, description):
    expenses = load_expenses()
    expense = {
        'id': len(expenses) + 1,
        'amount': float(amount),
        'description': description,
        'date': datetime.now().isoformat()
    }
    expenses.append(expense)
    save_expenses(expenses)
    print(f"Expense added: {description} - ${amount}")


def list_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses recorded.")
        return
    print("ID | Date | Amount | Description")
    print("-" * 40)
    for exp in expenses:
        date = datetime.fromisoformat(exp['date']).strftime('%Y-%m-%d')
        print(f"{exp['id']} | {date} | ${exp['amount']:.2f} | {exp['description']}")


def summary():
    expenses = load_expenses()
    total = sum(exp['amount'] for exp in expenses)
    print(f"Total expenses: ${total:.2f}")


def delete_expense(expense_id):
    expenses = load_expenses()
    expenses = [exp for exp in expenses if exp['id'] != int(expense_id)]
    save_expenses(expenses)
    print(f"Expense {expense_id} deleted.")


def main():
    parser = argparse.ArgumentParser(description="Expense Tracker CLI")
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Add command
    add_parser = subparsers.add_parser('add', help='Add a new expense')
    add_parser.add_argument('amount', type=float, help='Expense amount')
    add_parser.add_argument('description', help='Expense description')

    # List command
    subparsers.add_parser('list', help='List all expenses')

    # Summary command
    subparsers.add_parser('summary', help='Show total expenses')

    # Delete command
    delete_parser = subparsers.add_parser('delete', help='Delete an expense by ID')
    delete_parser.add_argument('id', type=int, help='Expense ID')

    args = parser.parse_args()

    if args.command == 'add':
        add_expense(args.amount, args.description)
    elif args.command == 'list':
        list_expenses()
    elif args.command == 'summary':
        summary()
    elif args.command == 'delete':
        delete_expense(args.id)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
