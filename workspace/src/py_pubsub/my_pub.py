import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('/my_topic', String, queue_size=10)
    rospy.init_node('my_node', anonymous=True)
    rate = rospy.Rate(10)  # 10 Hz

    while not rospy.is_shutdown():
        message = "Hello, Bartek Ksel!"
        rospy.loginfo(message)
        pub.publish(message)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass