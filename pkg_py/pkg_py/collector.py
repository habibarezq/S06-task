#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Float32 
from weather_interfaces.srv import MonitorData
class aggregatorNode(Node):
    def __init__(self):
        super().__init__("collector")
        self.subscriber_temp_=self.create_subscription(Float32,"Temperature",self.callback_temp,10)
        self.subscriber_pres_=self.create_subscription(Float32,"pressure",self.callback_pressure,10)
        self.subscriber_humidity_=self.create_subscription(Float32,"humidity",self.callback_humidity,10)

        self.reset_aggregated_data()
        self.get_logger().info("Data Collection Has been Started!!")


    def reset_aggregated_data(self):
         self.temperature = 0.0
         self.pressure = 0.0
         self.humidity = 0.0


    def callback_temp(self,msg):
        self.temperature=msg.data
        self.get_logger().info(f"Temperature is {self.temperature:.2f} °C")
        self.call_WeatherData ()


    def callback_pressure(self,msg):
        self.pressure=msg.data
        self.get_logger().info(f"Pressure is {self.pressure:.2f} atm")
        self.call_WeatherData ()


    def callback_humidity(self,msg):
        self.humidity = msg.data
        self.get_logger().info(f"Humidity is {self.humidity:.2f} %")
        self.call_WeatherData ()

    def call_WeatherData (self):
        client = self.create_client(MonitorData, "WeatherData")
        while not client.wait_for_service(1.0): 
            self.get_logger().warn("Waiting for Server ....")
        
        request = MonitorData.Request()
        request.temperature = self.temperature
        request.pressure = self.pressure
        request.humidity = self.humidity

        future = client.call_async(request)
        future.add_done_callback( partial(self.callback_call_WeatherData))

    def callback_call_WeatherData (self, future):
        try:
            response = future.result()
            self.get_logger().info("The pressure response reached is " + str (response.pressok))
            self.get_logger().info("The temperature response reached is " + str (response.tempok))
            self.get_logger().info("The humidity response reached is " + str (response.humok))
        except Exception as e:
            self.get_logger().error("Service call failed %r" % (e,))

    def call_monitor_data_server(self):
        pass
def main(args=None):
    rclpy.init(args=args)
    node=aggregatorNode()
    rclpy.spin(node)
    rclpy.shutdown()
if __name__ =="__main__":
    main()

