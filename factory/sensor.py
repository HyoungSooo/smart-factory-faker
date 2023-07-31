import random
from sensor_data_generator.data_generator import SensorDataGenerator as sdg


class BaseSensor:
    def _get_values(self):
        pass


class Sensor(BaseSensor):
    def __init__(self, name, mean_value, sigma, distribution) -> None:
        self.name = name
        self.data_generator = sdg()
        self.data_generator.generation_input.add_option(sensor_names=name,
                                                        distribution=distribution,
                                                        mu=mean_value,
                                                        sigma=sigma)

    def _get_values(self):
        return self.data_generator.generate(sample_size=1)[self.name].values.tolist()[0]

    def _get_data_generator(self):
        return self.data_generator.data


class BoolSensor(BaseSensor):
    def __init__(self, name, true_rate):
        self.name = name
        self.true_rate = true_rate

    def _get_values(self):
        flag_value = random.random()

        if flag_value >= self.true_rate:
            return True

        return False
