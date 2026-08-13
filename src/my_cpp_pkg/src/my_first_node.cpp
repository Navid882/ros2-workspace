#include "rclcpp/rclcpp.hpp" 

// ctrl+shif+p then c/c++ edit configuration json
// then copy the path opt/ros/lyrical/include/** 
// under iclude path section
class MyNode: public rclcpp::Node
{
    public:
        MyNode(): Node("cpp_test"), counter_(0)
        {
            RCLCPP_INFO(this->get_logger(), "Hello cpp node");
            timer_ = this->create_wall_timer(std::chrono::seconds(3),
                                        std::bind(&MyNode::timerCallback, this));        }
    private:
        void timerCallback()
        {
            counter_++;
            RCLCPP_INFO(this->get_logger(), "Hello!! %d", counter_);
        }
        rclcpp::TimerBase::SharedPtr timer_;
        int counter_;        
};

int main (int argc, char **argv)

{
    rclcpp::init(argc,argv);
    auto node=std::make_shared<MyNode>();
    // auto node=std::make_shared<rclcpp::Node>("cpp_test");//make the node using shared pointer
    // RCLCPP_INFO(node->get_logger(), "Hello cpp node");//print sth
    rclcpp::spin(node);//make alive
    rclcpp::shutdown();
    return 0;

}
// we need to copmile first then install it
// go to cmakelist.txt
// then we go this address ~/ros2_ws/install/my_cpp_pkg/lib/my_cpp_pkg and run the code ./cpp_node
