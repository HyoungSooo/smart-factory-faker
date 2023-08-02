import random
from Faker.sensor_data_generator.data_generator import SensorDataGenerator as sdg
from .sensor_helper import SensorHelper


class BaseSensor:

    def __init__(self):
        self.sensor_helper = SensorHelper()
        self.__necessary_params = list()

        for key, params in self.sensor_helper.prams.items():
            self.__necessary_params.append(key)

    def _get_values(self):
        pass

    def _check_for_important_parameters(self, params={}):

        indicator = 0
        for param in self.__necessary_params:
            if param in params.keys():
                if type(params[param]) == str:
                    raise TypeError(f"{param} must not be sting")
                indicator += 1

        if indicator == 0:
            raise ValueError(
                "one of the following parameters must be specified:", self.__necessary_params)

        return params


class Sensor(BaseSensor):
    def __init__(self, name, payload) -> None:
        self.name = name
        self.data_generator = sdg()
        self.data_generator.generation_input.add_option(sensor_names=name,
                                                        **payload)
        self.option = {}

        super().__init__()

    def _get_values(self):
        random_value = random.random()
        if self.option.get('error_condition', None) and random_value < self.option.get('error_condition'):
            return False, 'error condition'

        generated_data = self.data_generator.generate(
            sample_size=1)[self.name].values.tolist()[0]

        for key, value in self.option.items():
            if key == 'break_condition_low' and value > generated_data:
                return False, 'break_condition_low'
            elif key == 'break_condition_high' and value < generated_data:
                return False, 'break_condition_high'

        return True, generated_data

    def _get_data_generator(self):
        return self.data_generator.data

    def view_sensor_data_plot(self, count):
        self.data_generator.generate(sample_size=count)

        self.data_generator.plot_data()

    def add_option(self, **kwargs):
        params = self._check_for_important_parameters(kwargs)
        value = params.get('error_condition', None)
        if not value:
            params.update({'error_condition': 0})
        self.option = params

        return self
