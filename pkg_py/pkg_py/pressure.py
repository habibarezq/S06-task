#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Float32 
import random

class PressureNode(Node):
    
    def __init__(self):
        super().__init__("pressure")
        self.publisher_=self.create_publisher(Float32,"pressure",10)
        self.timer=self.create_timer(5,self.publish_pressure)
        self.get_logger().info("Pressure has been published!!")

    def publish_pressure(self):
        msg=Float32()
        msg.data=self.get_pressure() #0.95atm<=p<=1.2atm
        self.publisher_.publish(msg)


    def get_pressure(self):
        return random.uniform(0.75,1.4)
    
    
def main(args=None):
    rclpy.init(args=args)
    node=PressureNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "main":
    main()