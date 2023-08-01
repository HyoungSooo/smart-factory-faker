# Smart Factory Faker

### how to use
```shell
<clone this repotitory>
```

This is a project that can build a fake data set with a process.
You can define the route of the process and by defining the sensor, you can build a data set of the process in progress.

### Tutorial
* [Tutorial](https://github.com/HyoungSooo/smart-factory-faker/blob/main/tutorial.ipynb)

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

### V 0.7.0
* Sensor data can be visualized as a plot

### V 0.7.1
* Refactoring the code

### V 0.7.2
* fixed bug