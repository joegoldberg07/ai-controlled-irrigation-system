import random
import time
from datetime import datetime


class BaseSensor:
    def __init__(self, sensor_id, location):
        self.sensor_id = sensor_id
        self.location = location
        self.last_reading = None

    def get_timestamp(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def status(self):
        return {
            "sensor_id": self.sensor_id,
            "location": self.location,
            "last_reading": self.last_reading
        }


class SoilMoistureSensor(BaseSensor):
    def read(self):
        value = random.randint(20, 90)
        self.last_reading = value
        return value


class TemperatureSensor(BaseSensor):
    def read(self):
        value = round(random.uniform(18.0, 42.0), 2)
        self.last_reading = value
        return value


class HumiditySensor(BaseSensor):
    def read(self):
        value = random.randint(30, 95)
        self.last_reading = value
        return value


class PHLevelSensor(BaseSensor):
    def read(self):
        value = round(random.uniform(5.5, 8.5), 2)
        self.last_reading = value
        return value


class LightSensor(BaseSensor):
    def read(self):
        value = random.randint(100, 1000)
        self.last_reading = value
        return value


class SensorManager:
    def __init__(self):
        self.sensors = []

    def register_sensor(self, sensor):
        self.sensors.append(sensor)

    def collect_all(self):
        readings = []

        for sensor in self.sensors:
            readings.append({
                "sensor": sensor.sensor_id,
                "value": sensor.read(),
                "timestamp": sensor.get_timestamp()
            })

        return readings

    def print_report(self):
        readings = self.collect_all()

        print("=" * 60)
        print("SENSOR REPORT")
        print("=" * 60)

        for item in readings:
            print(
                f"[{item['timestamp']}] "
                f"{item['sensor']} -> {item['value']}"
            )

        print("=" * 60)

    def sensor_count(self):
        return len(self.sensors)


def initialize_default_sensors():
    manager = SensorManager()

    manager.register_sensor(
        SoilMoistureSensor("SM-001", "Field-A")
    )

    manager.register_sensor(
        SoilMoistureSensor("SM-002", "Field-B")
    )

    manager.register_sensor(
        SoilMoistureSensor("SM-003", "Field-C")
    )

    manager.register_sensor(
        TemperatureSensor("TMP-001", "Field-A")
    )

    manager.register_sensor(
        TemperatureSensor("TMP-002", "Field-B")
    )

    manager.register_sensor(
        HumiditySensor("HUM-001", "Field-A")
    )

    manager.register_sensor(
        HumiditySensor("HUM-002", "Field-B")
    )

    manager.register_sensor(
        PHLevelSensor("PH-001", "Field-A")
    )

    manager.register_sensor(
        LightSensor("LUX-001", "Field-A")
    )

    return manager


def monitor_loop():
    manager = initialize_default_sensors()

    while True:
        manager.print_report()
        time.sleep(10)


if __name__ == "__main__":
    manager = initialize_default_sensors()
    manager.print_report()


