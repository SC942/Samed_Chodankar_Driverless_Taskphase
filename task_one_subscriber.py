import rclpy
from rclpy.node import Node
from custom_interfaces.msg import TaskOne

class TaskOneSubscriber(Node):
    def __init__(self):
        super().__init__("task_one_subscriber")
        self.subscription = self.create_subscription(
            TaskOne, "/taskone", self.listener_callback, 10
        )
        self.get_logger().info("Task one subscriber node has been initialised.")

    def listener_callback(self, msg):
        longitudinal_speed = msg.ang_vel * msg.radius
        self.get_logger().info(
            f"Received -> Angular Velocity: {msg.ang_vel}, Radius: {msg.radius} | "
            f"Calculated Longitudinal Speed: {longitudinal_speed:.2f} m/s"
        )

def main(args=None):
    rclpy.init(args=args)
    node = TaskOneSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()