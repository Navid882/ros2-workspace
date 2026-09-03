#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

class Mynode(Node):
        def __init__(self):
             super().__init__("py_test")
             self.counter_= 0
             self.get_logger().info("Hello_ros2")
             self.create_timer(0.5, self.timer_callback)
        def timer_callback(self):
             self.counter_+= 1
             #self.get_logger().info("Hello")
             self.get_logger().info ("Hello!"+str(self.counter_))

def main(args=None):
    rclpy.init(args=args)
    node=Mynode()
    #node=Node("py_test")#create a node by Node constructor inside the file
    #node.get_logger().info("Hello_ros2")#The like print function
    rclpy.spin(node)
    rclpy.shutdown()#remove evvrything 

if __name__ == '__main__':
    main()


