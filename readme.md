# Smart Factory Faker

### how to use
```shell
<clone this repotitory>
```

This is a project that can build a fake data set with a process.
You can define the route of the process and by defining the sensor, you can build a data set of the process in progress.

quick starter

```python
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
              fa1.name: Or([0, 1], [fa2, fa3]),
              fa2.name: SeqLoop(fa4),
              fa3.name: SeqLoop(fa4),
              fa4.name: SeqLoop(fa5),
              fa5.name: Or([0, 1], node=[fa6, fa7]),
              fa6.name: SeqLoop(fa5),
              fa7.name: None
          })
df = k.to_dataframe(10) -> Dataframe
df_to_csv = k.to_csv(10, path='./res.csv') -> CSV
df_by_fa = k.by_facility(10) -> dict(key: facility name, value: DataFrame)

```
quick starter process map
![image](https://github.com/HyoungSooo/smart-factory-faker/assets/86239441/bfcd35ca-6b70-4d3e-b33c-7fe06172cd29)



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

### V 0.3.1
* Create BoolSensor