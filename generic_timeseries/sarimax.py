from typing import Tuple
from generic_timeseries.predictor import Predictor
from generic_timeseries.time_series import TimeSeries
from generic_timeseries.types import TimeTick


class Sarimax(Predictor[TimeTick]):
    def __init__(self, order: Tuple[int, int, int], sorder: Tuple[int, int, int], trend="n"):
        self.order = order
        self.sorder = sorder
        self.trend = trend

    def fit(self, data: TimeSeries[TimeTick, float]):
        pass
