# Importa la clase Expense desde el módulo models del mismo paquete
from .models import Expense
# Importa funciones para cargar y guardar gastos desde/hacia disco
from .storage import load_expenses, save_expenses

def add_expense(amount: float, description: str, category: str):
    """
    Agrega un nuevo gasto al sistema.
    Parámetros: monto, descripción y categoría del gasto.
    Retorna: el objeto Expense creado.
    """
    # Carga todos los gastos existentes desde el archivo
    expenses = load_expenses()
    # Crea un nuevo objeto Expense con los datos proporcionados
    # La fecha se genera automáticamente
    expense = Expense(amount=amount, description=description, category=category)
    # Añade el nuevo gasto a la lista de gastos
    expenses.append(expense)
    # Guarda la lista actualizada en el archivo
    save_expenses(expenses)
    # Retorna el gasto creado para que pueda ser usado (ej: mostrar confirmación)
    return expense



def list_expenses():
    """Devuelve todos los gastos guardados."""
    # Simplemente retorna la lista completa de gastos desde el almacenamiento
    return load_expenses()


def delete_expense(expense_id: int) -> bool:
    """
    Elimina el gasto en la posición expense_id (basado en 1-index, como se muestra al listar).
    Retorna True si se eliminó, False si el id es inválido.
    """
    # Carga todos los gastos desde el archivo
    expenses = load_expenses()
    # Verifica que el ID esté dentro del rango válido (entre 1 y el número total de gastos)
    if 1 <= expense_id <= len(expenses):
        # Elimina el gasto en la posición indicada
        # Resta 1 porque Python usa índices base-0 pero mostramos al usuario números base-1
        del expenses[expense_id - 1]
        # Guarda la lista actualizada sin el gasto eliminado
        save_expenses(expenses)
        # Retorna True indicando que la eliminación fue exitosa
        return True
    # Si el ID no es válido, retorna False
    return False


def summarize_expenses(month: int = None):
    """
    Calcula el total de gastos.
    Si se proporciona 'month', solo suma los gastos de ese mes específico.
    Parámetros: month (opcional) - número de mes (1-12)
    Retorna: suma total de los montos
    """
    # Carga todos los gastos desde el archivo
    expenses = load_expenses()
    # Si no se especificó un mes, suma todos los gastos
    if month is None:
        # sum() suma todos los montos usando una expresión generadora
        # e.amount obtiene el monto de cada gasto
        total = sum(e.amount for e in expenses)
        return total
    # Si se especificó un mes, filtra los gastos de ese mes
    # e.date tiene formato "2025-11-04T14:30:00"
    # e.date[5:7] extrae los caracteres en posición 5 y 6 que representan el mes ("11")
    # int() convierte el string a número para comparar con el parámetro month
    filtered = [e for e in expenses if int(e.date[5:7]) == month]
    # Suma solo los gastos filtrados del mes especificado
    total = sum(e.amount for e in filtered)
    return total