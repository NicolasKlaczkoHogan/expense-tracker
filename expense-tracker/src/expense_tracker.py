#!/usr/bin/env python3
"""
Expense Tracker CLI Application

A simple command-line tool to track personal expenses.
Helps users manage their finances by recording, viewing, and summarizing expenses.
"""

import argparse
import json
import os
import urllib.parse
import urllib.request
from datetime import datetime

DATA_FILE = 'expenses.json'
API_URL = 'https://api.exchangerate.host/latest'


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


def get_exchange_rate(base_currency, target_currency):
    target_currency = target_currency.upper()
    params = urllib.parse.urlencode({
        'base': base_currency.upper(),
        'symbols': target_currency,
    })
    url = f"{API_URL}?{params}"

    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            data = json.load(response)
    except Exception as exc:
        raise RuntimeError(f"Failed to fetch exchange rate: {exc}")

    if not data.get('success', True):
        raise RuntimeError('Exchange rate API returned an error')

    rates = data.get('rates', {})
    if target_currency not in rates:
        raise ValueError(f"Currency '{target_currency}' not found in API response")

    return float(rates[target_currency])


def convert_expenses(target_currency, base_currency='BRL'):
    expenses = load_expenses()
    total = sum(exp['amount'] for exp in expenses)
    rate = get_exchange_rate(base_currency, target_currency)
    converted = total * rate

    print(f"Total expenses: {total:.2f} {base_currency}")
    print(
        f"Converted to {target_currency.upper()}: {converted:.2f} "
        f"{target_currency.upper()} (rate: {rate:.4f})"
    )


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

    # Convert command
    convert_parser = subparsers.add_parser(
        'convert', help='Convert total expenses from BRL to another currency'
    )
    convert_parser.add_argument(
        'currency', help='Target currency code, e.g. USD or EUR'
    )

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
    elif args.command == 'convert':
        convert_expenses(args.currency)
    elif args.command == 'delete':
        delete_expense(args.id)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
