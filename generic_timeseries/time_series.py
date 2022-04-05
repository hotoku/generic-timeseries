from dataclasses import dataclass
from typing import Generic, Sequence

from .types import TimeTick, Value


@dataclass
class TimeSeries(Generic[TimeTick, Value]):
    time: Sequence[TimeTick]
    value: Sequence[Value]
