#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Float32 , String
from weather_interfaces.msg import AggregatedData
class aggregatorNode(Node):
    def __init__(self):
        super().__init__("collector")
        self.subscriber_temp_=self.create_subscription(Float32,"Temperature",self.callback_temp,10)
        self.subscriber_pres_=self.create_subscription(Float32,"pressure",self.callback_pressure,10)
        self.subscriber_humidity_=self.create_subscription(Float32,"humidity",self.callback_humidity,10)
        self.aggregated_data = AggregatedData()
        
        # Initialize data to None
        self.reset_aggregated_data()
        self.get_logger().info("Data Collection Has been Started!!")

    def reset_aggregated_data(self):
        self.aggregated_data.temperature = None
        self.aggregated_data.pressure = None
        self.aggregated_data.humidity = None


    def callback_temp(self,msg):
        self.aggregated_data.temperature=msg.data
        self.get_logger().info(f"Temperature is {self.aggregated_data.temperature:.2f} °C")
        self.check_data() 

    def callback_pressure(self,msg):
        self.aggregated_data.pressure=msg.data
        self.get_logger().info(f"Pressure is {self.aggregated_data.pressure:.2f} atm")
        self.check_data() 

    def callback_humidity(self,msg):
        self.aggregated_data.humidity=msg.data
        self.get_logger().info(f"Humidity is {self.aggregated_data.humidity:.2f} %")
        self.check_data() 

    def check_data(self): #checks if all info has been collected before sending it
        pass


    def call_monitor_data_server(self):
        pass
def main(args=None):
    rclpy.init(args=args)
    node=aggregatorNode()
    rclpy.spin(node)
    rclpy.shutdown()
if __name__ =="__main__":
    main()

#        if(msg.data[0]==1 ):
#            if(msg.data[1]>=10 and msg.data[1]<=100):
#               self.get_logger().info("Sensor is working  & Temperature is " + str(msg.data[1]) + "°C")
#            else:
#               self.get_logger().info("Sensor is working but Temperature out of Range!!")
#        else:
#           self.get_logger().info("Sensor Failed!!") 
