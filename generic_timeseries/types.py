from typing import TypeVar
from datetime import date

from mdweek import Week


TimeTick = TypeVar("TimeTick", date, Week)
Value = TypeVar("Value")
