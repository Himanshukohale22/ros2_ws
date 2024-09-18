import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from std_msgs.msg import Int32

class CompanySubscriber(Node):

    def __init__(self):
        super().__init__('company_subscriber')

        # Subscribers for each topic
        self.sub_name = self.create_subscription(String, '/fynd/company_name', self.name_callback, 10)
        self.sub_age = self.create_subscription(Int32, '/fynd/company_age', self.age_callback, 10)
        self.sub_employees = self.create_subscription(Int32, '/fynd/company_employees', self.employees_callback, 10)

    def name_callback(self, msg):
        self.get_logger().info('Received founder name: "%s"' % msg.data)

    def age_callback(self, msg):
        self.get_logger().info('Received company age: "%d" years' % msg.data)

    def employees_callback(self, msg):
        self.get_logger().info('Received number of employees: "%d"' % msg.data)

def main(args=None):
    rclpy.init(args=args)
    sub = CompanySubscriber()
    rclpy.spin(sub)
    sub.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()