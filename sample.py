from sensor_data_generator.data_generator import SensorDataGenerator as sdg
from factory.facility import Facility
from factory.sensor import Sensor

from factory.gate import *
from process.processor import Processor
from process.processor_stack import CallStackProcessor
from miner.visualize import ProcessVisualize, PlotData

normal = {
    'distribution': 'normal',
    'mu': 0,
    'sig': 1,
}

uniform = {
    'distribution': 'uniform',
    'lo': 0,
    'hi': 1
}
payload = {
    'break_condition_low': 0,
    'error_condition': 0
}

fa1 = Facility('test1', Sensor(
    'test_sensor1', normal).add_option(**payload), time=1)
fa2 = Facility('test2', Sensor('test_sensor2', normal), time=2)
fa3 = Facility('test3', Sensor('test_sensor3', normal), time=3)
fa4 = Facility('test4', Sensor('test_sensor4', normal), time=5)
fa5 = Facility('test5', Sensor('test_sensor5', uniform), time=10)
fa6 = Facility('test6', Sensor('test_sensor6', uniform), time=5)
fa7 = Facility('test7', Sensor('test_sensor7', uniform), time=50)
fa8 = Facility('test8', Sensor('test_sensor8', uniform), time=50)

route = {
    fa1.name: Or([0.5, 0.5], [fa2, fa3]),
    fa2.name: SeqLoop(fa4),
    fa3.name: SeqLoop(fa4),
    fa4.name: SeqLoop(fa5),
    fa5.name: Or([0.1, 0.9], node=[fa6, fa7]),
    fa6.name: SeqLoop(fa5),
    fa7.name: None
}

j = CallStackProcessor(start_node=fa1,
                       route=route)

df = j.to_dataframe(100)

print(j.break_points)
ProcessVisualize('./', 'test', 'text graph',
                       'test').huristic_visualizer(start_node=fa1, route=route, df=df, veiw_sensor=True, view_now=True)
# PlotData().sensor_data_view_plot(df, 'test_sensor1')
