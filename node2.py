import rclpy
from rclpy.node import Node
from custom_interfaces.msg import RT2String
from std_msgs.msg import Int32

class PalindromeCheckerNode(Node):
    def __init__(self):
        super().__init__("node2")
        self.subscription = self.create_subscription(
            RT2String, "/rt2_string_topic", self.string_callback, 10
        )
        self.publisher_ = self.create_publisher(Int32, "/palindrome_result_topic", 10)
        self.get_logger().info("Node 2 has been started.")

    def string_callback(self, msg):
        text = msg.data
        cleaned_text = text.replace(" ", "").lower()
        is_pal = 1 if cleaned_text == cleaned_text[::-1] else 0
        
        result_msg = Int32()
        result_msg.data = is_pal
        self.publisher_.publish(result_msg)
        self.get_logger().info(f'Checked string "{text}" -> Palindrome result published: {is_pal}')

def main(args=None):
    rclpy.init(args=args)
    node = PalindromeCheckerNode()
    rclpy.spin(node)
    rclpy.shutdown()