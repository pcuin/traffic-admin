# python -m pytest 
from Traffic import *

class TestTraffic:

    def test_init(self):

        d = TrafficRank(1.99, "Low", 0, 1)
        assert d.carpool == False
        assert d.risk == 1
        assert d.rkey == "Low"
        assert d.radius == 1
        assert d.speed == 1

    def test_get_liability(self):

        d = TrafficRank(1.99, "Low", 0, 1)
        assert d.get_liability() == d.risk

