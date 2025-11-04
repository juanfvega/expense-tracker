"""
Data models for expenses and budgets.
"""

from dataclasses import dataclass
from datetime import datetime

@dataclass
class Expense:
    amount: float
    description: str
    category: str
    date: datetime