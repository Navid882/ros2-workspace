#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String


class RobotNewsStationNode(Node):
    def __init__(self):
        super().__init__("robot_news_station")
        self.declare_parameter("robot_name", "C3PO")
        self.robot_name_ = self.get_parameter("robot_name").value

        self.publisher_ = self.create_publisher(String, "robot_news", 10) #type,name of topic, buffer size
        self.timer_ = self.create_timer(0.5, self.publish_news)#2hertz
        self.get_logger().info("Robot News Station has been started")#good to add this 

    def publish_news(self):
        msg = String()
        msg.data = (
            "Hi, this is " + str(self.robot_name_) + " from the Robot News Station."
        )
        self.publisher_.publish(msg)
def main(args=None):
    rclpy.init(args=args)
    node = RobotNewsStationNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()

#add in setup.py this: "robot_news_station = my_py_pkg.robot_news_station:main"
#ros2 interface show example_interfaces/msg/String : this ready message will be use
#also need add dependencies in package.xml.   <depend>example_interfaces</depend>
#test this command ros2 topic list, ros2 node list, ros2 topic echo /robot_news