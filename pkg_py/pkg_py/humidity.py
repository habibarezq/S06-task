#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Float32 
import random

class HumidityNode(Node):
    
    def __init__(self):
        super().__init__("humidity")
        self.publisher_=self.create_publisher(Float32,"humidity",10)
        self.timer=self.create_timer(5,self.publish_humidity)
        self.get_logger().info("Humidity has been published!!")

    def publish_humidity(self):
        msg=Float32()
        msg.data=self.get_humidity() #0.7<=h<=0.95
        self.publisher_.publish(msg)


    def get_humidity(self):
        return random.uniform(0.5,1.15)
    
    
def main(args=None):
    rclpy.init(args=args)
    node=HumidityNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "main":
    main()