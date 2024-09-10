#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Float32 , String
class aggregatorNode(Node):
    def __init__(self):
        super().__init__("collector")
        self.subscriber_temp_=self.create_subscription(Float32,"Temperature",self.callback_temp,10)
        self.subscriber_pres_=self.create_subscription(Float32,"pressure",self.callback_pressure,10)
        self.get_logger().info("Data Collection Has been Started!!")
    def callback_temp(self,msg):
        self.get_logger().info(f"Temperature is {msg.data:.2f} °C")
    def callback_pressure(self,msg):
        self.get_logger().info(f"Pressure is {msg.data:.2f} atm")
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