# !/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Float32 ,String
import random
class TemperatureNode(Node):
    def __init__(self):
        super().__init__("temp_node")
        self.publisher_=self.create_publisher(Float32,"Temperature",10)
        self.error_status_=self.create_publisher(String,"temperature_error",10)
        self.timer=self.create_timer(5,self.publish_temp)
        #self.publish_temp()
        self.get_logger().info("Temprature has been published!!")
    def publish_temp(self):
        msg=Float32()
        msg.data=self.get_temperature() #temperature ranges from 10°C to 100°C
        self.publisher_.publish(msg)

        if self.error():
            error_msg=String()
            error_msg.data="Error in Temperature Sensor"
            self.error_status_.publish(error_msg)
    def get_temperature(self):
        return random.uniform(0,110)
    def error(self):
        return False
def main(args=None):
    rclpy.init(args=args)
    node=TemperatureNode()
    rclpy.spin(node)
    rclpy.shutdown()
if __name__ =="__main__":
    main()