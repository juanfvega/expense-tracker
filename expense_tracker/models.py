# Importa dataclass para crear clases con menos código boilerplate
# field permite personalizar campos con valores por defecto especiales
from dataclasses import dataclass, asdict, field
# Importa datetime para manejar fechas y horas
from datetime import datetime
# Importa tipos para anotaciones de tipo (mejora la legibilidad y ayuda con el análisis estático)
from typing import List, Optional

# @dataclass es un decorador que genera automáticamente métodos como __init__, __repr__, __eq__
@dataclass
class Expense:
    # Monto del gasto (número decimal)
    amount: float
    # Descripción textual del gasto (ej: "Café", "Libro")
    description: str
    # Categoría del gasto (ej: "Comida", "Transporte")
    category: str
    # Fecha del gasto en formato ISO (ej: "2025-11-04T14:30:00")
    # field con default_factory genera automáticamente la fecha actual al crear un gasto
    # lambda: crea una función anónima que se ejecuta cada vez que se crea un objeto
    date: str = field(default_factory=lambda: datetime.now().isoformat())