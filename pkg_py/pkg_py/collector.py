#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int8  #UInt8 is signed 8 bits integer
class aggregatorNode(Node):
    def __init__(self):
        super().__init__("collector")
        self.subscriber_=self.create_subscription(Int8,"Temperature",self.callback,10)
        self.get_logger().info("Data Collection Has been Started!!")
    def callback(self,msg):
        self.get_logger().info("Temperature is " + str(msg.data) + "°C")
def main(args=None):
    rclpy.init(args=args)
    node=aggregatorNode()
    rclpy.spin(node)
    rclpy.shutdown()
if __name__ =="__main__":
    main()