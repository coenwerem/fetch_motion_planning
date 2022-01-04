#! /usr/bin/env python

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_group_python_interface_tutorial', anonymous=True)

robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()    
group = moveit_commander.MoveGroupCommander("arm")

# Useful Data
# Reference frame
print ("Reference frame: %s" % group.get_planning_frame())

# End effector link
print ("End effector: %s" % group.get_end_effector_link())

# List with all robot groups
print ("Robot Groups:")
print (robot.get_group_names())

# Current joint values
print ("Current Joint Values:")
print (group.get_current_joint_values())

##! Current end-effector pose (useful for real-time control)
print ("Current End-effector Pose:")
print (group.get_current_pose())

# Robot State
print ("Robot State:")
print (robot.get_current_state())


rospy.sleep(5)

moveit_commander.roscpp_shutdown()