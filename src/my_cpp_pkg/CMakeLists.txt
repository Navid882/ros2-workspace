cmake_minimum_required(VERSION 3.20)
project(my_cpp_pkg)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# Find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(example_interfaces REQUIRED)
find_package(my_robot_interfaces REQUIRED)

# Build executable
add_executable(cpp_node src/my_first_node.cpp)
target_link_libraries(cpp_node PUBLIC rclcpp::rclcpp)

add_executable(robot_news_station src/robot_news_station.cpp)
target_link_libraries(robot_news_station PUBLIC rclcpp::rclcpp example_interfaces::example_interfaces__rosidl_typesupport_cpp)

add_executable(smartphone src/smartphone.cpp)

target_link_libraries(smartphone PUBLIC 
  rclcpp::rclcpp 
  example_interfaces::example_interfaces__rosidl_typesupport_cpp
)
add_executable(add_two_ints_server src/add_two_ints_server.cpp)
target_link_libraries(add_two_ints_server PUBLIC 
  rclcpp::rclcpp
  example_interfaces::example_interfaces__rosidl_typesupport_cpp)

add_executable(add_two_ints_client_basic src/add_two_ints_client_basic.cpp)
target_link_libraries(add_two_ints_client_basic PUBLIC
   rclcpp::rclcpp
   example_interfaces::example_interfaces__rosidl_typesupport_cpp)

add_executable(add_two_ints_client src/add_two_ints_client.cpp)
target_link_libraries(add_two_ints_client PUBLIC 
  rclcpp::rclcpp
  example_interfaces::example_interfaces__rosidl_typesupport_cpp)

add_executable(hw_status_publisher src/hw_status_publisher.cpp)
target_link_libraries(hw_status_publisher PUBLIC
   rclcpp::rclcpp 
   my_robot_interfaces::my_robot_interfaces__rosidl_typesupport_cpp)
# Install executable
install(
  TARGETS
    cpp_node
    robot_news_station
    smartphone
    add_two_ints_server
    add_two_ints_client_basic
    add_two_ints_client
    hw_status_publisher
  DESTINATION lib/${PROJECT_NAME}
)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  set(ament_cmake_copyright_FOUND TRUE)
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()