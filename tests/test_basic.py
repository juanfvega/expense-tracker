import os
import tempfile
import json
import shutil
import pytest
from pathlib import Path
from expense_tracker import logic, models, storage

@pytest.fixture(autouse=True)
def temp_data_file(monkeypatch):
    # Usa un archivo temporal para no interferir con los datos reales
    with tempfile.TemporaryDirectory() as tmpdir:
        temp_path = Path(tmpdir) / "test_data.json"
        monkeypatch.setattr(storage, "DATA_FILE", temp_path)
        yield

def test_add_and_list_expense():
    assert logic.list_expenses() == []
    e = logic.add_expense(50, "Cena", "Comida")
    all_exp = logic.list_expenses()
    assert len(all_exp) == 1
    assert all_exp[0].amount == 50
    assert all_exp[0].description == "Cena"
    assert all_exp[0].category == "Comida"

def test_summarize_expenses():
    logic.add_expense(10, "Gaseosa", "Bebida")
    logic.add_expense(30, "Almuerzo", "Comida")
    total = logic.summarize_expenses()
    assert total == 40

def test_delete_expense():
    logic.add_expense(9, "Kiosco", "Snacks")
    logic.add_expense(1, "Lápiz", "Utiles")
    all_exp = logic.list_expenses()
    assert len(all_exp) == 2
    result = logic.delete_expense(1)  # Elimina el primero
    assert result == True
    restante = logic.list_expenses()
    assert len(restante) == 1
    assert restante[0].description == "Lápiz"

def test_summarize_expenses_by_month():
    from datetime import datetime
    # Agrega un gasto en agosto y otro en septiembre
    aug = models.Expense(amount=10, description="Galleta", category="Snacks", date="2025-08-10T13:00:00")
    sep = models.Expense(amount=20, description="Libro", category="Utiles", date="2025-09-01T17:00:00")
    storage.save_expenses([aug, sep])
    total_aug = logic.summarize_expenses(month=8)
    total_sep = logic.summarize_expenses(month=9)
    assert total_aug == 10
    assert total_sep == 20

def test_delete_expense_invalid_id():
    logic.add_expense(5, "Soda", "Bebida")
    result = logic.delete_expense(10)  # No hay ID 10
    assert result == False

def test_list_no_expenses():
    assert logic.list_expenses() == []