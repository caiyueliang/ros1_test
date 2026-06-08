#include <ros/ros.h>
#include <std_msgs/String.h>

int main(int argc, char *argv[])
{    
    ros::init(argc, argv, "yao_node");
    // 创建ROS节点句柄，用于与ROS系统通信，管理节点资源
    ros::NodeHandle nh;
    printf("ros init success !\n");

    // 创建发布者，用于发布消息，参数为: nh.advertise<std_msgs::消息类型>(话题名称, 缓存队列大小)
    ros::Publisher pub = nh.advertise<std_msgs::String>("yao_topic", 10);
    
    ros::Rate loop_rate(1.0); // 1Hz

    while(ros::ok())
    {    
        std_msgs::String msg;
        msg.data = "yao: test";
        pub.publish(msg);
        
        printf("sleep 1s ...\n");
        loop_rate.sleep(); // 暂停1秒
    }
    return 0;
}
