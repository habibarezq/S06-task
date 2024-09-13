#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from weather_interfaces.srv import MonitorData

class weatherForecastServer (Node):
    def __init__(self):
        super().__init__("server")
        self.server = self.create_service(MonitorData, "WeatherData", self.callback)

        self.get_logger().info("Server is up")

    def callback (self, request, response):
        
        if (request.temperature is None):
            response.tempok = 0                                         # 0 means no data from sensor
            self.get_logger().error("No temperature data")
        elif (request.temperature < 10 or request.temperature > 100):
            self.get_logger().warn(f"Temperature {request.temperature:.2f} is out of range")
            response.tempok = 1                                         # 1 means data is out of range
        else :
            self.get_logger().info(f"Temperature {request.temperature:.2f} is within range")
            response.tempok = 2                                         # 2 means data is within range

        if (request.pressure is None):
            response.pressok = 0                                         # 0 means no data from sensor
            self.get_logger().error("No presssure data")
        elif (request.pressure < 0.95 or request.pressure > 1.2):
            self.get_logger().warn(f"Pressure {request.pressure:.2f} is out of range")
            response.pressok = 1                                         # 1 means data is out of range
        else :
            self.get_logger().info(f"Pressure {request.pressure:.2f} is within range")
            response.pressok = 2                                         # 2 means data is within range

        if (request.humidity is None):
            response.humok = 0                                         # 0 means no data from sensor
            self.get_logger().error("No humidity data")
        elif (request.humidity < 0.7 or request.humidity > 0.95):
            self.get_logger().warn(f"Humidity {request.humidity:.2f} is out of range")
            response.humok = 1                                         # 1 means data is out of range
        else :
            self.get_logger().info(f"Humidity {request.humidity:.2f} is within range")
            response.humok = 2                                         # 2 means data is within range

        return response


def main(args=None):
    rclpy.init(args=args)
    node=weatherForecastServer()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ =="__main__":
    main()