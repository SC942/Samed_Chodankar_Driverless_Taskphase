#!/usr/bin/env/ python3

import rclpy
from rclpy.node import Node
from custom_interfaces.msg import TaskOne

class TaskOnePublisher(Node):
    def __init__(self):
        super().__init__("task_one_publisher")
        self.publisher_ = self.create_publisher(TaskOne, "/taskone", 10)
        self.get_logger().info("Task one publisher node has been initialised.")
        self.publish_data()

    def publish_data(self):
        while rclpy.ok():
            try:
                ang_vel_input = float(input("Enter angular velocity: "))
                radius_input = float(input("Enter radius: "))

                msg = TaskOne()
                msg.ang_vel = ang_vel_input
                msg.radius = radius_input

                self.publisher_.publish(msg)
                self.get_logger().info(f"Published- Angular velocity: {ang_vel_input}, Radius: {radius_input}")
            except ValueError:
                print("Enter valid numerical values.")

def main(args=None):
    rclpy.init(args=args)
    node = TaskOnePublisher()
    rclpy.spin(node)
    rclpy.shutdown()