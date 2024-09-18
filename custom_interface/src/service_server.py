#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from custom_interface.srv import Custom
from std_msgs.msg import String


class AboutCompanyInfo(Node):
    def __init__(self):
        super().__init__('about_company_server')
        self.srv = self.create_service(Custom,"get_info",self.handle_service)



    def handle_service(self,request,response):
        response.founder = String()
        response.founder.data = 'faruk'
        response.age_of_company = 12
        response.number_of_employee = 1500

        self.get_logger().info(f'Service request received')
        return response
    
def main(args=None):
    rclpy.init(args=args)
    node = AboutCompanyInfo()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ =="__main__":
    main()