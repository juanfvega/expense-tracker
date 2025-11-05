# Importa json para leer/escribir archivos en formato JSON
import json
# Importa Path para manejar rutas de archivos de manera multiplataforma
from pathlib import Path
# Importa List para anotar que la función retorna una lista
from typing import List
# Importa la clase Expense desde models
from .models import Expense

# Define la ubicación del archivo de datos
# Path.home() obtiene el directorio home del usuario (ej: /home/usuario)
# El operador / concatena rutas de manera segura independiente del sistema operativo
DATA_FILE = Path.home() / ".expense_tracker_data.json"

def load_expenses() -> List[Expense]:
    """
    Carga todos los gastos desde el archivo JSON en disco.
    Retorna: lista de objetos Expense (vacía si no existe el archivo)
    """
    # Verifica si el archivo existe en el sistema de archivos
    if not DATA_FILE.exists():
        # Si no existe, retorna una lista vacía (primera vez que se usa la app)
        return []
    # Abre el archivo en modo lectura ("r")
    # with garantiza que el archivo se cierre automáticamente al terminar
    with open(DATA_FILE, "r") as f:
        # json.load() lee el contenido del archivo y lo convierte de JSON a Python
        # data será una lista de diccionarios: [{}, {}, ...]
        data = json.load(f)
    # List comprehension: convierte cada diccionario en un objeto Expense
    # **item desempaqueta el diccionario como argumentos nombrados
    # Si item = {"amount": 50, "description": "Café", ...}
    # Entonces Expense(**item) es equivalente a Expense(amount=50, description="Café", ...)
    return [Expense(**item) for item in data]

def save_expenses(expenses: List[Expense]):
    """
    Guarda la lista de gastos en el archivo JSON en disco.
    Parámetros: expenses - lista de objetos Expense a guardar
    """
    # Abre el archivo en modo escritura ("w")
    # Si el archivo existe, lo sobrescribe; si no existe, lo crea
    with open(DATA_FILE, "w") as f:
        # Convierte la lista de objetos Expense a formato JSON y lo escribe en el archivo
        # e.__dict__ convierte cada objeto Expense en un diccionario con todos sus atributos
        # [e.__dict__ for e in expenses] crea una lista de diccionarios
        # indent=2 formatea el JSON con indentación de 2 espacios (más legible para humanos)
        json.dump([e.__dict__ for e in expenses], f, indent=2)