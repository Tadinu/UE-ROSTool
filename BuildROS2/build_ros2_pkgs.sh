#!/bin/bash
# Copyright 2020-2022 Rapyuta Robotics Co., Ltd.

Help()
{
    # Display Help
    echo "Syntax: ${BASH_SOURCE[0]} [-h] <UE_PATH> <ROS2_PKGS_WS> <PKGS>"
    echo "options:"
    echo "-h Print this Help."
    echo "arguments:"
    echo "-UE_PATH: Path to the UnrealEngine dir"
    echo "-ROS2_PKGS_WS: Path to target ROS2 pkg workspace"
    echo "-PKGS: Name of the target ROS2 pkgs"
}

while getopts ":h" option; do
    case $option in
        h) # display Help
            Help
            exit;;
        \?) # Invalid option
            echo "Error: Invalid option"
            Help
            exit;;
    esac
done

# Set exit on any non-zero status cmd
set -e

# Verify input dirs
check_empty() {
    if [[ "" == "$1" ]]; then
        printf "[$2] is empty!"
        Help
        exit 1
    fi
}
check_dir_valid() {
    check_empty $1 $2
    if [[ ! -d "$1" ]]; then
        printf "[$2] does not exist!"
        Help
        exit 1
    fi
}

ROS2_WS=$1
PKGS=$2
ROS2_PKGS_WS=$2
check_dir_valid $ROS2_PKGS_WS "ROS2_PKGS_WS"

# cleanup
for d in $2 ; 
do
    rm -r  $1/build/$d
    rm -r  $1/install/$d
done

export LANG=en_US.UTF-8

# Build ROS2 PKGS by UE clang toolchain
# export ROS_DOMAIN_ID=10
# pay attention it can be 'rmw_fastrtps_dynamic_cpp' too
export RMW_IMPLEMENTATION=rmw_fastrtps_cpp

# use locally installed clang-15 (Ubuntu 22)
export CC="/usr/bin/clang-15"
export CXX="/usr/bin/clang++-15"


# -latomic issue - see more here https://github.com/ros2/ros2/issues/418
export LINKER_FLAGS="-latomic "\
"-Wl,-rpath=\${ORIGIN} "\
"-Wl,-rpath-link=/usr/lib/x86_64-linux-gnu "\
"-Wl,-rpath-link=/usr/lib "

pushd $ROS2_WS
    colcon build \
        --packages-skip-build-finished \
        --packages-up-to $PKGS \
        --cmake-args \
            "-DCMAKE_SHARED_LINKER_FLAGS='$MY_LINKER_FLAGS'" \
            "-DCMAKE_EXE_LINKER_FLAGS='$MY_LINKER_FLAGS'" \
            -DBUILD_TESTING=OFF --no-warn-unused-cli
popd
    colcon build --packages-select $PKGS --cmake-args ${CMAKE_ARGS}
fi