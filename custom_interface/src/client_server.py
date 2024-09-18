#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from custom_interface.srv import Custom

class CompanyInfoClient(Node):
    def __init__(self):
        super().__init__('about_company_client')
        self.cli = self.create_client(Custom, 'get_info')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service not available, waiting...')
        self.request = Custom.request()

    def send_request(self):
        self.future = self.cli.call_async(self.request)   # when service send request 
        rclpy.spin_until_future_complete(self, self.future)  # 
        response = self.future.result()
        if response is not None:
            self.get_logger().info(f'Response received: Founder - {response.founder.data}, '
                                   f'Age - {response.age_of_company}, '
                                   f'Employees - {response.number_of_employee}')
        else:
            self.get_logger().error('Service call failed')

def main(args=None):
    rclpy.init(args=args)
    client = CompanyInfoClient()
    client.send_request()
    client.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
