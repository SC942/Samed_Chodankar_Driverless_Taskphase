import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32, String

class EvaluatorNode(Node):
    def __init__(self):
        super().__init__("node3")
        self.subscription = self.create_subscription(
            Int32, "/palindrome_result_topic", self.evaluation_callback, 10
        )
        self.response_publisher = self.create_publisher(String, "/node3_response_topic", 10)
        self.get_logger().info("Node 3 has been started.")

    def evaluation_callback(self, msg):
        reply = String()
        if msg.data == 1:
            reply.data = "Yes"
        else:
            reply.data = "No"
            
        self.response_publisher.publish(reply)
        print(f"Node 3 Terminal Output -> Received input: {msg.data} | Conveyed response: {reply.data}")

def main(args=None):
    rclpy.init(args=args)
    node = EvaluatorNode()
    rclpy.spin(node)
    rclpy.shutdown()