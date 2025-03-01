# SPDX-FileCopyrightText: 2025 Hikaru Nemoto 　　　　　
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
import subprocess
from rclpy.node import Node
from std_msgs.msg import String

def get_cpu_usage():
    result = subprocess.run("vmstat 1 2 | awk 'NR==3 {print $13, $14, $15}'", capture_output=True, text=True, shell=True)
    output = result.stdout.strip().split()
    
    if len(output) == 3:
        user_cpu = output[0]
        system_cpu = output[1]
        idle_cpu = output[2]
        
        return f"User CPU: {user_cpu}%, System CPU: {system_cpu}%, Idle CPU: {idle_cpu}%"
    else:
        return "Failed to retrieve CPU usage data."

def cb():
    cpu_usage = get_cpu_usage()
    msg = String()
    msg.data = cpu_usage
    pub.publish(msg)

def main():
    rclpy.init()
    global node, pub
    node = Node("cpuutilization")
    pub = node.create_publisher(String, "cpu_usage", 10)
    node.create_timer(3.0, cb)
    rclpy.spin(node)

