# !/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int8MultiArray
import random
class TemperatureNode(Node):
    def __init__(self):
        super().__init__("temp_node")
        self.publisher_=self.create_publisher(Int8MultiArray,"Temperature",10)
        self.timer=self.create_timer(5,self.publish_temp)
        self.get_logger().info("Temprature has been published!!")
    def publish_temp(self):
        msg=Int8MultiArray()
        msg.data[0]=1 #error status
        msg.data[1]= random.randint(10,100) #temperature ranges from 10°C to 100°C
        self.publisher_.publish(msg)
def main(args=None):
    rclpy.init(args=args)
    node=TemperatureNode()
    rclpy.spin(node)
    rclpy.shutdown()
if __name__ =="__main__":
    main()