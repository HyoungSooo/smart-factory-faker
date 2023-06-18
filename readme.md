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

fa1 = Facility('test1', Sensor('test_sensor1', 1, 0))
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

print(k.route)
df = k.to_dataframe(10)
print(df)

# result
#token_id facility                 @timestamp  test_sensor1  test_sensor3  test_sensor2  test_sensor4  test_sensor5  test_sensor6  test_sensor7
#0   XEYHB2MFRD    test1 2023-06-19 22:07:39.492403      0.552032           NaN           NaN           NaN           NaN           NaN           NaN
#1   NFW9NKEH7Z    test1 2023-06-19 22:07:40.492403      0.120843           NaN           NaN           NaN           NaN           NaN           NaN
#2   7VVAZZH273    test1 2023-06-19 22:07:41.492403      0.281798           NaN           NaN           NaN           NaN           NaN           NaN
#3   M28REE9JSW    test1 2023-06-19 22:07:42.492403      0.500399           NaN           NaN           NaN           NaN           NaN           NaN
#4   XFY6MNDB4E    test1 2023-06-19 22:07:43.492403      0.188721           NaN           NaN           NaN           NaN           NaN           NaN
#..         ...      ...                        ...           ...           ...           ...           ...           ...           ...           ...
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

#### V 0.0.1
* define process
* define facilities, and sensors
* return to dataframe