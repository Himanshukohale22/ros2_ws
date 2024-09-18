#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from custom_m.msg import CustomMessage

class company_info(Node):
    def __init__(self):
       super().__init__('company_info')

       self.publisher = self.create_publisher(CustomMessage,'/fynd/company_info',10)
       timer_period = 0.1 
       self.timer = self.create_timer(timer_period,self.timer_callback)

    def timer_callback(self):
        msg = CustomMessage()
        msg.founder = String()
        msg.founder.data = 'faruk'
        msg.age_of_company = 12 
        msg.number_of_employee = 1500

        self.publisher.publish(msg)


        self.get_logger().info('Publishing founder name: "%s"' % msg.founder.data)
        self.get_logger().info('Publishing company age: "%d" years' % msg.age_of_company)
        self.get_logger().info('Publishing number of employees: "%d"' % msg.number_of_employee)

def main(args=None):
    rclpy.init(args=args)
    pub = company_info()
    rclpy.spin(pub)
    pub.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()