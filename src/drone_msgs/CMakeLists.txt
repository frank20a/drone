cmake_minimum_required(VERSION 3.8)
project(drone_msgs)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/MotorPercs.msg"
  "msg/MotorCmd.msg"
  "msg/BuzzerCmd.msg"
  "msg/DateTime.msg"
  "msg/MotorLvls.msg"
  "msg/ControlFlags4.msg"
  "msg/DroneSetpoint4.msg"
  # "srv/AddThreeInts.srv"
)

ament_package()