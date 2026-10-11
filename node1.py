import rclpy
from rclpy.node import Node
from custom_interfaces.msg import RT2String

class StringPublisherNode(Node):
    def __init__(self):
        super().__init__("node1")
        self.publisher_ = self.create_publisher(RT2String, "/rt2_string_topic", 10)
        self.get_logger().info("Node 1 has been started.")
        self.publish_strings()

    def publish_strings(self):
        while rclpy.ok():
            user_input = input("Enter a string: ")
            msg = RT2String()
            msg.data = user_input
            self.publisher_.publish(msg)
            self.get_logger().info(f"Published string: {msg.data}")

def main(args=None):
    rclpy.init(args=args)
    node = StringPublisherNode()
    rclpy.spin(node)
    rclpy.shutdown()