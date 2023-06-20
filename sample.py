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
              fa1.name: Or([0, 1], [fa2, fa3]),
              fa2.name: SeqLoop(fa4),
              fa3.name: SeqLoop(fa4),
              fa4.name: SeqLoop(fa5),
              fa5.name: Or([0, 1], node=[fa6, fa7]),
              fa6.name: SeqLoop(fa5),
              fa7.name: None
          })
# df = k.to_dataframe(10)
# df_to_csv = k.to_csv(10, path='./res.csv')
df_by_fa = k.by_facility(100)
print(df_by_fa)
