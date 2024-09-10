#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Float32 , String
import random
class PressureNode(Node):
    
    def __init__(self):
        super().__init__("pressure")
        self.publisher_=self.create_publisher(Float32,"pressure",10)
        self.error_status_=self.create_publisher(String,"pressure_error",10)
        self.timer=self.create_timer(1,self.publish_pressure)
        self.get_logger().info("Pressure has been published!!")

    def publish_pressure(self):
        msg=Float32()
        msg.data=self.get_pressure() #0.95atm<=p<=1.2atm
        self.publisher_.publish(msg)

        if self.error():
            error_msg=String()
            error_msg.data="Error in Pressure Sensor"
            self.error_status_.publish(error_msg)

    def get_pressure(self):
        return random.uniform(0.95,1.2)
    
    def error(self):
        return False
    
def main(args=None):
    rclpy.init(args=args)
    node=PressureNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "main":
    main()