class SensorHelper:
    def __init__(self):
        self.prams = {
            'break_condition_low': 'int(Decide whether to stop below a certain value)',
            'break_condition_high': 'int(Decide whether to stop above a certain value)',
            'error_condition': 'Defines the probability of an error occurring (0 to 1, Default is 0)'
        }
