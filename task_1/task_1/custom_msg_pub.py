
import rclpy
from rclpy.node import Node

from task_1.msg import company


class CompanyInfo(Node):

    def __init__(self):
        super().__init__('company_info')
        self.node_publisher = self.create_publisher(company, '/fynd/company_details', 10)

        timer_period = 0.1  # 10 Hz
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        # Publishing the founder's name
        company_msg = company()
        company_msg.founder = "farook"
        company_msg.age_of_company = 12
        company_msg.number_of_employees = 1500
        
        self.node_publisher.publish(company)

        self.get_logger().info('founder: %s ' %company_msg.founder)
        self.get_logger().info('age_of_company: %d years' %company_msg.age_of_company)
        self.get_logger().info('number_of_employee :  %d ' %company_msg.number_of_employee) 


def main(args=None):
    rclpy.init(args=args)
    pub = CompanyInfo()
    rclpy.spin(pub)
    pub.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
