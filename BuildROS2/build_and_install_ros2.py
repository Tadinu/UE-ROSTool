#!/usr/bin/env python3

import os, time
from libs_utils import *

def build_ros2(
    buildType,
    allowed_pkgs = [],
    pkgs = [],
    ros_ws = os.path.join(os.getcwd(), '../ros2_ws'),
    remove = True,
    rosdistro = 'humble'
):
    
    buildRosScript =  os.path.join(os.getcwd(), 'setup_ros2_' + buildType + '.sh')

    allowed_pkgs.extend(pkgs)

    if remove:
        if os.path.exists(ros_ws):
            print('Cleanup workspace')
            shutil.rmtree(ros_ws)



    print('Building ros ' + buildType + '...')
    os.system('chmod +x ' + buildRosScript)
    os.system('bash ' + buildRosScript + ' ' + ros_ws + ' ' + rosdistro + ' ' +  ' "' + ' '.join(pkgs) + '"')

def install_ros2(
    projectPath,
    pluginName,
    pluginFolderName, #pluginFolderName is not always same as pluginName
    targetThirdpartyFolderName,
    buildType,
    ros_ws,
    allowed_pkgs = [],
    not_allowed_pkgs = [],
    remove = False,
    rosdistro = 'humble'
):
    # Assume pluginFolderName is same as PluginName if it is empty.
    if pluginFolderName == '':
        pluginFolderName = pluginName

    # ros paths
    rosInstall  = os.path.join(ros_ws, 'install')

    # UE paths
    pluginPath =  os.path.join(projectPath, 'Plugins', pluginFolderName)
    pluginPathBinaries = os.path.join(pluginPath, 'Binaries')
    pluginPathRos =  os.path.join(pluginPath, 'ThirdParty', targetThirdpartyFolderName)
    pluginPathRosInclude =  os.path.join(pluginPathRos, 'include')
    pluginPathRosLib =  os.path.join(pluginPathRos, 'lib')
    pluginPathBuildCS =  os.path.join( pluginPath, 'Source', pluginName, pluginName + '.Build.cs')
    projectPathBinaries =  os.path.join(projectPath, 'Binaries' )

    if remove:
        if os.path.exists(ros_ws):
            print('Cleanup workspace')
            shutil.rmtree(ros_ws)

    if remove:
        if os.path.exists(pluginPathRosInclude):
            shutil.rmtree(pluginPathRosInclude)
        if os.path.exists(pluginPathRosLib):
            shutil.rmtree(pluginPathRosLib)

    os.makedirs(pluginPathRosInclude, exist_ok=True)
    os.makedirs(pluginPathRosLib, exist_ok=True)

    print('Grabbing includes...')
    GrabIncludes(rosInstall, pluginPathRosInclude, allowed_pkgs)
    CleanIncludes(pluginPathRosInclude, not_allowed_pkgs)

    if buildType == 'base':
        print('Applying includes patch...')
        os.system('cd ' + pluginPath + '; git apply ' + 
                    os.path.join(os.getcwd(), 'patches', rosdistro, 'rcutils.patch'))

    print('Grabbing libs...')
    GrabLibs(rosInstall, pluginPathRosLib, allowed_pkgs)
    CleanLibs(pluginPathRosLib, not_allowed_pkgs)

    LocalizeLibSymbols(pluginPathRosLib, projectPath)
    InvalidateBinaries(projectPathBinaries, pluginPathBinaries, pluginPathBuildCS)
    RemovePyDependency(pluginPathRosLib, projectPath)
    # You also can try this:
    # CreateInfoForAll('objdump -x', pluginPathRosLib, infoRosOutput) # see also 'ldd'
    # CheckLibs(pluginPathRosLib)

if __name__ == '__main__':
    print("Please use build_ros function from other wrapper.")

