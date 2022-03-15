from datetime import datetime
from decimal import Decimal
from numpy import average
import requests


class TemperatureDayService:
    @staticmethod
    def get_temperature(date):
        dateConvertered = datetime.strptime(date, "%Y-%m-%d")
        result = requests.get(
            f"https://www.metaweather.com/api/location/523920/{dateConvertered.year}/{dateConvertered.month}/{dateConvertered.day}/").json()

        temperatures = []

        for x in result:
            if x['created'][0:10] == date:

                temperatures.append(x['the_temp'])

        sum_temperature = 0

        for x in temperatures:
            sum_temperature += x

        average_temperature = sum_temperature / len(temperatures)
        return average_temperature
