#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Float32MultiArray
import random
class PressureNode(Node):
    def __init__(self):
        super().__init__("pressure")
        self.publisher_=self.create_publisher(Float32MultiArray,"pressure",10)
        self.timer=self.create_timer(5,self.publish_pressure)
        self.error_status=1
        self.get_logger().info("Pressure has been published!!")
    def publish_pressure(self):
        msg=Float32MultiArray()
        self.error_status=random.randint(0,1)
        msg.data.append(self.error_status)
        msg.data.append(random.uniform(0.95,1.2)) #0.95atm<=p<=1.2atm
        self.publisher_.publish(msg)
def main(args=None):
    rclpy.init(args=args)
    node=PressureNode()
    rclpy.spin(node)
    rclpy.shutdown()
if __name__ == "main":
    main()