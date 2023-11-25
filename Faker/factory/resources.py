class ResourcesHelper:
    def __init__(self):
        self.prams = {
            'name': 'str',
            'time': 'int(Runing Time)',
        }


class Resources:
    def __init__(self) -> None:
        self.resources_helper = ResourcesHelper()
        self.__necessary_params = []
        self.resources = []

        for key, params in self.resources_helper.prams.items():
            self.__necessary_params.append(key)

    def _check_for_important_parameters(self, params={}):

        if not params.get('name', None) or not params.get('time', None):
            raise ValueError(
                "name and time is required check the dictionary keys")

        if type(params['name']) != str or type(params['time']) != int:
            raise ValueError("check values type (name => str, time => int)")

        return params

    def add_resource(self, **payload):
        params = self._check_for_important_parameters(payload)

        self.resources.append((params.get('name'), params.get('time')))

        return
