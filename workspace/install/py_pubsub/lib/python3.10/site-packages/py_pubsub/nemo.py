import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class Node_Nemo(Node):

    def __init__(self):
        super().__init__('Nemo')
        self.publisher_temp = self.create_publisher(String, '/nemo/temp', 10)
        self.publisher_depth = self.create_publisher(String, '/nemo/depth', 10)

def main(args=None):
    rclpy.init(args=args)
    nemo = Node_Nemo()

    while rclpy.ok():
        print("Simulation for CAN temperature data sending (enter value of temperature):")
        msg = String()
        msg.data = str(input())
        nemo.publisher_temp.publish(msg)
        nemo.get_logger().info('Published temp: "%s"' % msg.data)
        
        print("Simulation for CAN depth data sending (enter value of depth):")
        msg = String()
        msg.data = str(input())
        nemo.publisher_depth.publish(msg)
        nemo.get_logger().info('Published depth: "%s"' % msg.data)
        
        rclpy.spin_once(nemo)

    nemo.publisher_depth.destroy()
    nemo.publisher_temp.destroy()
    nemo.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
