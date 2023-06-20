# Smart Factory Faker

### how to use
```shell
<clone this repotitory>
```

quick starter

```python
from factory.facility import Facility
from factory.sensor import Sensor

from process.gate import *
from process.route import Route

fa1 = Facility('test1', Sensor('test_sensor1', 1, 0),
               Sensor('fa1 test_sessor', 10, 2))
fa2 = Facility('test2', Sensor('test_sensor2', 1, 0))
fa3 = Facility('test3', Sensor('test_sensor3', 1, 0))
fa4 = Facility('test4', Sensor('test_sensor4', 1, 0))
fa5 = Facility('test5', Sensor('test_sensor5', 1, 0))
fa6 = Facility('test6', Sensor('test_sensor6', 1, 0))
fa7 = Facility('test7', Sensor('test_sensor7', 1, 0))
fa8 = Facility('test8', Sensor('test_sensor8', 1, 0))

k = Route(start_node=fa1,
          route={
              fa1.name: Or(fa2, fa3),
              fa2.name: SeqLoop(fa4),
              fa3.name: SeqLoop(fa4),
              fa4.name: SeqLoop(fa5),
              fa5.name: Or(fa6, fa7),
              fa6.name: SeqLoop(fa5),
              fa7.name: None
          })
df = k.to_dataframe(10) -> Dataframe
df_to_csv = k.to_csv(10, path='./res.csv') -> CSV
df_by_fa = k.by_facility(10) -> dict(key: facility name, value: DataFrame)

```



A smart factory has a process also you can define the process.

### Route

Route class

```python
class Route:
    def __init__(self, start_node, route) -> None:
        self.start_node = start_node
        self.route = route
        self.logs = []
        self.token_id_len = 10
        self.senser_hash = {}
        self.senser_pointer = 0

k = Route(start_node=fa1,
          route={
            ...
              fa1.name: Or(fa2, fa3),
              fa2.name: SeqLoop(fa4),
              fa3.name: SeqLoop(fa4),
              fa4.name: SeqLoop(fa5),
              fa5.name: Or(fa6, fa7),
              fa6.name: SeqLoop(fa5),
              fa7.name: None
            ...
          })
```
route must be a dictionary.

### Gates

```python
class SeqLoop:
    def __init__(self, node) -> None:
        self.next = node

    def get_next_node(self):
        return self.next


class Or:
    def __init__(self, *node) -> None:
        self.next = node

    def get_next_node(self):
        return random.choice(self.next)
```
SepLoop is a combination of sequence and loop gates.
An OR gate is a gate that selects one of the facilities that make up the OR gate.

### version

#### V 0.1.0
* define process
* define facilities, and sensors
* return to dataframe

#### V 0.2.0
* return to csv
* return by facilies (it will return to seperated datafram by facilities)

### V 0.2.1
* Or gate can difine probability for branching
* raise erorr when branch probability is not define