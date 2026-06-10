#include <ros/ros.h>
#include <std_msgs/String.h>

void chao_callback(const std_msgs::String::ConstPtr& msg)
{
    ROS_INFO("[get chao topic] %s", msg->data.c_str());
}

void yao_callback(const std_msgs::String::ConstPtr& msg)
{
    ROS_WARN("[get yao topic] %s", msg->data.c_str());
}

int main(int argc, char *argv[])
{    
    // setlocale(LC_ALL, "zh_CN");
    setlocale(LC_ALL, "zh_CN.UTF-8");

    ros::init(argc, argv, "ma_node");
    // 创建ROS节点句柄，用于与ROS系统通信，管理节点资源
    ros::NodeHandle nh;
    ROS_INFO("ros init success !");

    // 创建发布者，用于发布消息，参数为: nh.advertise<std_msgs::消息类型>(话题名称, 缓存队列大小)
    //ros::Publisher pub = nh.advertise<std_msgs::String>("ma_topic", 10);
    // 创建订阅者，用于订阅消息，参数为: nh.subscribe<std_msgs::消息类型>(话题名称, 缓存队列大小, 回调函数)
    ros::Subscriber sub = nh.subscribe<std_msgs::String>("chao_topic", 10, &chao_callback);
    ros::Subscriber sub_2 = nh.subscribe<std_msgs::String>("yao_topic", 10, &yao_callback);

    // ros::Rate loop_rate(1.0); // 1Hz

    while(ros::ok())
    {    
        // 处理订阅者收到的消息
        ros::spinOnce();        // 查看是否有新消息，如果有则调用回调函数

        // std_msgs::String msg;
        // msg.data = "ma: hello world";
        // pub.publish(msg);
        
        // printf("sleep 1s ...\n");
        // loop_rate.sleep(); // 暂停1秒
    }
    return 0;
}
