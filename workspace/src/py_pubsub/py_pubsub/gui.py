import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class Node_GUI(Node):

    def __init__(self):
        super().__init__('GUI')
        self.subscriber_temp = self.create_subscription(
            String,
            '/nemo/temp',
            self.listen_temp,
            10)

        self.subscriber_depth = self.create_subscription(
            String,
            '/nemo/depth',
            self.listen_depth,
            10)

        self.subscriber_temp  # prevent unused variable warning

    def listen_temp(self, msg):
        self.get_logger().info('Temperature is t = "%s"' % msg.data)

    def listen_depth(self, msg):
        self.get_logger().info('Depth is d = "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)

    gui = Node_GUI()

    rclpy.spin(gui)

    gui.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()