#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

class Mynode(Node):#4rd
        def __init__(self):#4rd
             super().__init__("py_test")#4rd
             self.counter_= 0#6
             self.get_logger().info("Hello_ros2")#4rd
             self.create_timer(0.5, self.timer_callback)#5rd
        def timer_callback(self):#5rd
             self.counter_+= 1
             #self.get_logger().info("Hello")#5rd
             self.get_logger().info ("Hello!"+str(self.counter_))#6

def main(args=None):
    rclpy.init(args=args)
    node=Mynode()#4rd
    #node=Node("py_test")#create a node by Node constructor inside the file
    #node.get_logger().info("Hello_ros2")#The like print function
    rclpy.spin(node)#2nd step add because we need the node be alive
    rclpy.shutdown()#remove evvrything 

if __name__ == '__main__':
    main()

#we need chmod +x bfore run
#3rd step we need to install it to have more functionalty. we dont want every time run manulally like this ./my_first_node
#3rd colcon build and go this path /ros2_ws/install/my_py_pkg/lib/my_py_pkg and run ./py_node
#everytime start new terminal better to run source .bashrc
#3rd the run the code with ros2 command: ros2 my_py_pkg py_node