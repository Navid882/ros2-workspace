#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/msg/string.hpp"

class RobotNewsStationNode : public rclcpp::Node
{
public:
    RobotNewsStationNode() : Node("robot_news_station")
    {
        this->declare_parameter("robot_name", "R2D2");
        robot_name_ = this->get_parameter("robot_name").as_string();
        
        publisher_ = this->create_publisher<example_interfaces::msg::String>("robot_news", 10);
        timer_ = this->create_wall_timer(std::chrono::milliseconds(500),
                                         std::bind(&RobotNewsStationNode::publishNews, this));
        RCLCPP_INFO(this->get_logger(), "Robot News Station has been started.");
    }

private:
    void publishNews()
    {
        auto msg = example_interfaces::msg::String();
        msg.data = std::string("Hi, this is ") + robot_name_ + std::string(" from the Robot News Station");
        publisher_->publish(msg);
    }

    std::string robot_name_;
    rclcpp::Publisher<example_interfaces::msg::String>::SharedPtr publisher_;
    rclcpp::TimerBase::SharedPtr timer_;
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<RobotNewsStationNode>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}
// we must add <depend>example_interfaces</depend> in xml file
// also in Cmakelist.txt add find_package(example_interfaces REQUIRED)
// also add excutable in .txt file: add_executable(robot_news_station src/robot_news_station.cpp)
// target_link_libraries(robot_news_station PUBLIC rclcpp::rclcpp example_interfaces::example_interfaces__rosidl_typesupport_cpp)
//also add this under install:   robot_news_stationc