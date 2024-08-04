#!/usr/bin/env python3
import rclpy
from rclpy.node import Node


def main(args=None):
    """
    Entry point for the program.

    Args:
        args (List[str], optional): Command line arguments. Defaults to None.
    """
    rclpy.init(args=args)
    node = Node("py_test")
    node.get_logger().info("Hello Ros2")
    rclpy.spin(node)  # to keep the node alive until it is shutdown
    rclpy.shutdown()


if __name__ == "__main__":
    main()
