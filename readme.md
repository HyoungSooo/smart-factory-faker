# Smart Factory Faker

### how to use
```shell
<clone this repotitory>
```

This is a project that can build a fake data set with a process.
You can define the route of the process and by defining the sensor, you can build a data set of the process in progress.

quick starter

```python
from sensor_data_generator.data_generator import SensorDataGenerator as sdg
from factory.facility import Facility
from factory.sensor import Sensor, BoolSensor

from process.gate import *
from process.processor import Processor
from process.processor_stack import CallStackProcessor
from miner.visualize import ProcessVisualize

fa1 = Facility('test1', Sensor('test_sensor1', 1, 1, 'normal'),
               BoolSensor('fa1 test_sessor', 0.2), time=1)
fa2 = Facility('test2', Sensor('test_sensor2', 1, 1, 'normal'), time=2)
fa3 = Facility('test3', Sensor('test_sensor3', 1, 1, 'normal'), time=3)
fa4 = Facility('test4', Sensor('test_sensor4', 1, 1, 'normal'), time=5)
fa5 = Facility('test5', Sensor('test_sensor5', 1, 1, 'normal'), time=10)
fa6 = Facility('test6', Sensor('test_sensor6', 1, 1, 'normal'), time=5)
fa7 = Facility('test7', Sensor('test_sensor7', 1, 1, 'normal'), time=50)
fa8 = Facility('test8', Sensor('test_sensor8', 1, 1, 'normal'), time=50)

route = {
    fa1.name: Or([0.5, 0.5], [fa2, fa3]),
    fa2.name: SeqLoop(fa4),
    fa3.name: SeqLoop(fa4),
    fa4.name: SeqLoop(fa5),
    fa5.name: Or([0.2, 0.8], node=[fa6, fa7]),
    fa6.name: SeqLoop(fa5),
    fa7.name: None
}

j = CallStackProcessor(start_node=fa1,
                       route=route)

df = j.to_dataframe(100)
ProcessVisualize('./', 'test', 'text graph',
                       'test').huristic_visualizer(start_node=fa1, route=route, df=df, veiw_sensor=True, view_now=False)

```
quick starter visualizer result


![test](https://github.com/HyoungSooo/smart-factory-faker/assets/86239441/c8a04974-d46a-477b-b2f1-085fc20a36a9)


quick starter Huristic visualize result


![test](https://github.com/HyoungSooo/smart-factory-faker/assets/86239441/68ccfec6-4d0e-407d-b21b-479840b0bc5b)


View Process Map with sensor infomation


![test](https://github.com/HyoungSooo/smart-factory-faker/assets/86239441/1258d83d-6024-458d-a282-ebd25cd3dbb4)



Graphviz must be installed to visualize

### version

### V 0.1.0
* define process
* define facilities, and sensors
* return to dataframe

### V 0.2.0
* return to csv
* return by facilies (it will return to seperated datafram by facilities)

### V 0.2.1
* Or gate can difine probability for branching
* raise erorr when branch probability is not define

### V 0.3.0
* Create BoolSensor

### V 0.4.0
* Create method using heap(This function is more accurate Processor class is no longer maintained)

### V 0.4.1
* Can visualize the difined route

### v 0.5.0
* Huristic visualizer function is created(This function plots a number on a edge)

### V 0.5.1
* Visualizer can show sensor infomation

### V 0.6.0
* Sensor data can be generated for multiple distributions
* More sophisticated timestamps of sensor data generated by the process
