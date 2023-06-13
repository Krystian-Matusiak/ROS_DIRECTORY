import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class Node_PID(Node):

    def __init__(self):
        super().__init__('PID')

        self.subscriber_depth = self.create_subscription(
            String,
            '/nemo/depth',
            self.listen_depth,
            10)

        self.listen_depth  # prevent unused variable warning

    def listen_depth(self, msg):
        self.get_logger().info('Depth is d = "%s"' % msg.data)
        self.get_logger().info('PID is performed')

def main(args=None):
    rclpy.init(args=args)

    pid = Node_PID()

    rclpy.spin(pid)

    pid.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()