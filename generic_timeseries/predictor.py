from abc import ABC, abstractmethod
from typing import Generic
from generic_timeseries.time_series import TimeSeries

from generic_timeseries.types import TimeTick


class Predictor(ABC, Generic[TimeTick]):
    @abstractmethod
    def fit(self, data: TimeSeries[TimeTick, float]):
        return NotImplemented

    @abstractmethod
    def predict(self, n: int):
        return NotImplemented
