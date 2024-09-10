#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Float32 , String
import random
class HumidityNode(Node):
    
    def __init__(self):
        super().__init__("humidity")
        self.publisher_=self.create_publisher(Float32,"humidity",10)
        self.error_status_=self.create_publisher(String,"humidity_error",10)
        self.timer=self.create_timer(1,self.publish_humidity)
        self.get_logger().info("Humidity has been published!!")

    def publish_humidity(self):
        msg=Float32()
        msg.data=self.get_humidity() #0.7<=h<=0.95
        self.publisher_.publish(msg)

        if self.error():
            error_msg=String()
            error_msg.data="Error in Humidity Sensor"
            self.error_status_.publish(error_msg)

    def get_humidity(self):
        return random.uniform(0.7,0.95)
    
    def error(self):
        return False
    
def main(args=None):
    rclpy.init(args=args)
    node=HumidityNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "main":
    main()