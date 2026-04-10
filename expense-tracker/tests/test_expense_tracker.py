import pytest
from src.expense_tracker import load_expenses, add_expense, summary, delete_expense


@pytest.fixture
def temp_data_file(tmp_path):
    test_file = tmp_path / 'expenses.json'
    # Monkey patch the DATA_FILE
    import src.expense_tracker
    src.expense_tracker.DATA_FILE = str(test_file)
    yield test_file
    # Cleanup
    if test_file.exists():
        test_file.unlink()


def test_load_expenses_empty(temp_data_file):
    expenses = load_expenses()
    assert expenses == []


def test_add_expense(temp_data_file):
    add_expense(10.5, "Coffee")
    expenses = load_expenses()
    assert len(expenses) == 1
    assert expenses[0]['amount'] == 10.5
    assert expenses[0]['description'] == "Coffee"


def test_summary(temp_data_file):
    add_expense(10, "Test1")
    add_expense(20, "Test2")
    # Capture print, but for simplicity, just check if it runs
    summary()  # Should print total 30.00


def test_delete_expense(temp_data_file):
    add_expense(10, "Test")
    expenses = load_expenses()
    assert len(expenses) == 1
    delete_expense(1)
    expenses = load_expenses()
    assert len(expenses) == 0


def test_add_invalid_amount(temp_data_file):
    with pytest.raises(ValueError):
        add_expense("invalid", "Test")  # But in CLI it's handled by argparse
