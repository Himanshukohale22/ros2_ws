
// include all necessary lib
#include <memory>

//ros2 lib and std_msgs
#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"

// used when we need std::bind 
using std::placeholders::_1;

//create a class node

class  Minimalsubscriber :public rclcpp::Node
{
    public:
        Minimalsubscriber()
        : Node("minimal publisher")
        {
            subscription_ = this->create_subscription<std_msgs::msg::String>(
            "topic", 10, std::bind(&Minimalsubscriber::topic_callback, this,_1));
        }

    private:
        void topic_callback(const std_msgs::msg::String & msg){
            RCLCPP_INFO(this->get_logger(),"I hear: '%s'",msg.data.c_str());
        }
        rclcpp::Subscription<std_msgs::msg::String>::SharedPtr subscription_;

};
int main(int argc ,char * argv[]){
    rclcpp::init(argc,argv);
    rclcpp::spin(std::make_shared<Minimalsubscriber>());
    rclcpp::shutdown();
    return 0;

}

