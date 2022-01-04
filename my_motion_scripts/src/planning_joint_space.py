#! /usr/bin/env python

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_group_python_joint_space', anonymous=True)

robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()    
group = moveit_commander.MoveGroupCommander("arm")
display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory, queue_size=1)

group_variable_values = group.get_current_joint_values()

group_variable_values[5] = -1.5
group_variable_values[6] = 0.5
group.set_joint_value_target(group_variable_values)

plan2 = group.plan()
# Useful Data
# Reference frame
# print ("Reference frame: %s" % group.get_planning_frame())

# End effector link
# print ("End effector: %s" % group.get_end_effector_link())

# List with all robot groups
# print ("Robot Groups:")
# print (robot.get_group_names())

# Current joint values
# print ("Current Joint Values:")
# print (group.get_current_joint_values())

##! Current end-effector pose (useful for real-time control)
# print ("Current Pose:")
# print (group.get_current_pose())

# Robot State
# print ("Robot State:")
# print (robot.get_current_state())


rospy.sleep(5)

moveit_commander.roscpp_shutdown()