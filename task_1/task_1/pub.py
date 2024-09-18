import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from std_msgs.msg import Int32

class CompanyInfo(Node):

    def __init__(self):
        super().__init__('company_info')
        self.string_publisher = self.create_publisher(String, '/fynd/company_name', 10)
        self.int_publisher = self.create_publisher(Int32, '/fynd/company_age', 10)
        self.employee_publisher = self.create_publisher(Int32, '/fynd/company_employees', 10)

        timer_period = 0.1  # 10 Hz
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        # Publishing the founder's name
        string_msg = String()
        string_msg.data = "farook"
        self.string_publisher.publish(string_msg)

        # Publishing the company's age
        int_msg_age = Int32()
        int_msg_age.data = 12
        self.int_publisher.publish(int_msg_age)

        # Publishing the number of employees
        int_msg_employees = Int32()
        int_msg_employees.data = 1500
        self.employee_publisher.publish(int_msg_employees)

        self.get_logger().info('Publishing founder name: "%s"' % string_msg.data)
        self.get_logger().info('Publishing company age: "%d" years' % int_msg_age.data)
        self.get_logger().info('Publishing number of employees: "%d"' % int_msg_employees.data)

def main(args=None):
    rclpy.init(args=args)
    pub = CompanyInfo()
    rclpy.spin(pub)
    pub.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
