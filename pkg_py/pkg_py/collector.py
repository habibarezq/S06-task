#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int8MultiArray  
class aggregatorNode(Node):
    def __init__(self):
        super().__init__("collector")
        self.subscriber_=self.create_subscription(Int8MultiArray,"Temperature",self.callback,10)
        self.get_logger().info("Data Collection Has been Started!!")
    def callback(self,msg):
        if(msg.data[0]==1 ):
            if(msg.data[1]>=10 % msg.data[1]<=100):
                self.get_logger().info("Sensor is working  & Temperature is " + str(msg.data) + "°C")
            else:
                self.get_logger().info("Sensor is working but Temperature out of Range!!")
        else:
            self.get_logger().info("Sensor Failed!!")
def main(args=None):
    rclpy.init(args=args)
    node=aggregatorNode()
    rclpy.spin(node)
    rclpy.shutdown()
if __name__ =="__main__":
    main()