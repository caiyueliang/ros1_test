#include <ros/ros.h>

int main(int argc, char *argv[])
{    
    ros::init(argc, argv, "chao_node");
    ros::NodeHandle nh;
    printf("ros init success !\n");
    
    while(ros::ok())
    {    
        printf("sleep 1s ...\n");
        ros::Duration(1.0).sleep(); // 暂停1秒
    }
    return 0;
}
