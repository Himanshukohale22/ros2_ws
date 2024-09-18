#!/usr/bin/env python3
# import rclpy 
# from rclpy.node import Node 
# from custom_m.msg import CustomMessage

# class subs(Node):
#     def __init__(self):
#         super().__init__('subscriber')
#         self.subscription_ = self.create_subscription(CustomMessage,'/fynd/company_info',self.callback,10)

#         self.subscription_

#     def callback(self,msg):
#         self.get_logger().info('Fynd founder: %s' %msg.founder.data)
#         self.get_logger().info('Age of Company: %d' %msg.age_of_company)
#         self.get_logger().info('number of employees: %d' %msg.number_of_employee)
        
# def main(args=None):
#     rclpy.init(args=args)
#     rclpy.spin(subs)
#     subs.destroy_node()
#     rclpy.shutdown()

# if __name__ == '__main__':
#     main()

#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from custom_m.msg import CustomMessage  # Import the custom message

class CompanyInfoSubscriber(Node):
    def __init__(self):
        super().__init__('company_info_subscriber')
        self.subscription = self.create_subscription(
            CustomMessage,
            '/fynd/company_info',
            self.listener_callback,
            10
        )
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info(f'Received founder name: {msg.founder.data}')
        self.get_logger().info(f'Received company age: {msg.age_of_company}')
        self.get_logger().info(f'Received number of employees: {msg.number_of_employee}')

def main(args=None):
    rclpy.init(args=args)
    node = CompanyInfoSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
