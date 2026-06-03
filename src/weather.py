import random
from datetime import datetime, timedelta


class WeatherForecast:

    CONDITIONS = [
        "Sunny",
        "Cloudy",
        "Partly Cloudy",
        "Rain",
        "Thunderstorm",
        "Windy",
        "Fog"
    ]

    def __init__(self):
        self.forecast_data = []

    def generate_forecast(self, days=7):

        self.forecast_data.clear()

        for day in range(days):

            forecast_date = (
                datetime.now() + timedelta(days=day)
            ).strftime("%Y-%m-%d")

            forecast = {
                "date": forecast_date,
                "condition": random.choice(
                    self.CONDITIONS
                ),
                "temperature": random.randint(
                    22,
                    40
                ),
                "humidity": random.randint(
                    40,
                    95
                ),
                "rain_probability": random.randint(
                    0,
                    100
                )
            }

            self.forecast_data.append(forecast)

        return self.forecast_data

    def print_forecast(self):

        if not self.forecast_data:
            self.generate_forecast()

        print("=" * 60)
        print("WEATHER FORECAST")
        print("=" * 60)

        for item in self.forecast_data:

            print(
                f"{item['date']} | "
                f"{item['condition']} | "
                f"{item['temperature']}C | "
                f"Humidity {item['humidity']}% | "
                f"Rain {item['rain_probability']}%"
            )

        print("=" * 60)

    def should_irrigate_today(self):

        if not self.forecast_data:
            self.generate_forecast()

        today = self.forecast_data[0]

        if today["rain_probability"] > 60:
            return False

        return True

    def average_temperature(self):

        if not self.forecast_data:
            self.generate_forecast()

        total = 0

        for item in self.forecast_data:
            total += item["temperature"]

        return round(
            total / len(self.forecast_data),
            2
        )

    def average_humidity(self):

        if not self.forecast_data:
            self.generate_forecast()

        total = 0

        for item in self.forecast_data:
            total += item["humidity"]

        return round(
            total / len(self.forecast_data),
            2
        )


def weather_summary():

    weather = WeatherForecast()

    weather.generate_forecast(10)

    weather.print_forecast()

    print(
        "Average Temperature:",
        weather.average_temperature()
    )

    print(
        "Average Humidity:",
        weather.average_humidity()
    )

    print(
        "Irrigation Recommended:",
        weather.should_irrigate_today()
    )


if __name__ == "__main__":
    weather_summary()


