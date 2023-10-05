#!/usr/bin/env bash

ROS2_WS=$1
ROS_DISTRO=$2

# install dependency and get ros2 sources
source ./pre_build_ros2_base.sh $ROS2_WS $ROS_DISTRO

# build ros2
source ./build_ros2_base.sh $ROS2_WS
