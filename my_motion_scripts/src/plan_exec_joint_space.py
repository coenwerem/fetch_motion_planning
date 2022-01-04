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

# First Motion
pose_target = geometry_msgs.msg.Pose()
pose_target.orientation.w = 1.0
pose_target.position.x = 0.96
pose_target.position.y = 0
pose_target.position.z = 1.18
group.set_pose_target(pose_target)

# Plan & Exec 1
plan1 = group.plan()
group.go(wait=True)
rospy.sleep(5)

# Second Motion
group_variable_values = group.get_current_joint_values()

# Change joint values & assign to joint value target
group_variable_values[5] = -1.5
group_variable_values[6] = 0.5
group.set_joint_value_target(group_variable_values)

# Plan & Exec 2
plan2 = group.plan()
group.go(wait=True)

rospy.sleep(5)

moveit_commander.roscpp_shutdown()