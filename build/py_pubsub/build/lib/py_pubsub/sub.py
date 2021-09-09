import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

class MinimalSub(Node):

    def __init__(self):
        super().__init__('minimal_sub')
        self.subscription_ = self.create_subscription(Odometry, 'demo/odom_demo',self.listener_callback, 10)
        #self.subscription

    def listener_callback(self,msg):
        self.get_logger().info(('Linear: \n'
                                'x = {:.3f} \n'
                                'y = {:.3f} \n'
                                'z = {:.3f} \n'
                                'Angular: \n' 
                                'x = {:.3f} \n'
                                'y = {:.3f} \n'
                                'z = {:.3f} \n').format(msg.pose.pose.position.x,\
                                                    msg.pose.pose.position.y,\
                                                    msg.pose.pose.position.z,\
                                                    msg.pose.pose.orientation.x,\
                                                    msg.pose.pose.orientation.y,\
                                                    msg.pose.pose.orientation.z ))

def main(args=None):
    rclpy.init(args=args)

    minimal_sub = MinimalSub()

    rclpy.spin(minimal_sub)

    minimal_sub.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
