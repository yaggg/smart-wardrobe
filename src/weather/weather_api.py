import ast
import requests
from datetime import datetime


class WeatherAPI:

    def __init__(self):
        self.base_url = "https://api.openweathermap.org/data/2.5/weather?q="
        self.app_id = '2a18f509e5c6305b4a57639afa4d9ac5'

    @staticmethod
    def _to_celsius(temperature):
        # (K - 273,15) = С
        return temperature - 273.15

    @staticmethod
    def get_now_season():
        date = datetime.now()
        seasons = {'Summer': (datetime(2020, 6, 21), datetime(2020, 9, 22)),
                   'Autumn': (datetime(2020, 9, 23), datetime(2020, 12, 20)),
                   'Spring': (datetime(2020, 3, 21), datetime(2020, 6, 20))}
        for season, (season_start, season_end) in seasons.items():
            if date >= season_start and date <= season_end:
                return season
        else:
            return 'Winter'

    def get_temperature_by_city(self, city_name):
        print(self.base_url + city_name + '&appid=' + self.app_id)
        r = requests.get(self.base_url + city_name + '&appid=' + self.app_id)
        data = ast.literal_eval(r.text)
        temperature = self._to_celsius(data['main']['temp'])
        return temperature
