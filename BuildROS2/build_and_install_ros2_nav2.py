#!/usr/bin/env python3

import sys
import argparse

from build_and_install_ros2 import build_ros2

DEFAULT_ALLOWED_SPACES = [
    'nav2_amcl',
    #'nav2_behavior_tree',
    'nav2_bringup',
    #'nav2_bt_navigator',
    'nav2_common',
    'nav2_controller',
    'nav2_core',
    'nav2_costmap_2d',
    'nav2_dwb_controller',
    'nav2_lifecycle_manager',
    'nav2_map_server',
    'nav2_msgs',
    'nav2_navfn_planner',
    'nav2_planner',
    #'nav2_recoveries',
    'nav2_regulated_pure_pursuit_controller',
    #'nav2_rviz_plugins',
    'nav2_system_tests',
    'nav2_util',
    'nav2_voxel_grid',
    'nav2_waypoint_follower',
    'navigation2',
    ]
DEFAULT_NOT_ALLOWED_SPACES = [ 
    '.so.', 
    ]
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Build ros2 from source with necessasary patches to be used with UnrealEngine. And copy lib and header files under Unreal Project folder."
    )
    parser.add_argument(
        "--ue_path",
        help="Path to UE",
        required=True
    )
    parser.add_argument(
        "--ue_proj_path",
        help="Path to target UE project",
        required=True
    )
    parser.add_argument(
        "--ue_plugin_name",
        help="UE plugin module name, eg: rclUE",
        default='rclUE'
    )
    parser.add_argument(
        "--ue_plugin_folder_name",
        help="UE plugin folder name, eg: rclUE",
        default=''
    )
    parser.add_argument(
        "--ue_target_3rd_name",
        help="Target 3rd name under ThirdParty, eg: ros",
        default='ros'
    )
    args = parser.parse_args()

    ue_plugin_folder_name = args.ue_plugin_folder_name
    if ue_plugin_folder_name == '':
        ue_plugin_folder_name = args.ue_plugin_name

    build_ros2(
        UEPath = args.ue_path,
        projectPath = args.ue_proj_path,
        pluginName = args.ue_plugin_name,
        pluginFolderName = ue_plugin_folder_name,
        targetThirdpartyFolderName = args.ue_target_3rd_name,
        buildType = 'base',
        allowed_spaces = DEFAULT_ALLOWED_SPACES,
        not_allowed_spaces = DEFAULT_NOT_ALLOWED_SPACES,
        pkgs = ['ue_msgs'],
    )
