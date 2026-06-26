import rclpy
from rclpy.node import Node

if __name__ == '__main__':
    rclpy.init()
    node = Node('ros2_py_node')
    node.get_logger().info('Hello from ROS 2 Python Node!')
    rclpy.spin(node)

    node.get_logger().warn('停止，清理 Node')
    node.destroy_node()
    rclpy.shutdown()