from controller import Robot
import numpy as np
import cvxpy as cp
from ConstantsLib import ConstantsLib
from MovementsLib import MovementsLib
from ControlLib import ControlLib

# Webots setup
NAO6_robot = Robot()
timestep = int(NAO6_robot.getBasicTimeStep())

myConstantsLib = ConstantsLib
myControlLib = ControlLib.ModelPredictiveControl(timestep=timestep)
myJoints = myConstantsLib.joints()
myMovements = MovementsLib.movements()

NAO6_joints = myJoints.createNAO6Joints(NAO6_robot=NAO6_robot)
NAO6_sensors = myJoints.createNAO6Sensors(joints=NAO6_joints,
                                          timestep=timestep)

# Number of time steps for 1 minute of simulation
total_time = 600  # in seconds
steps_per_second = int(1000 / timestep)
total_steps = total_time * steps_per_second

current_step = 0
# Main loop to run the Webots simulation
while NAO6_robot.step(timestep) != -1:

    # Set the robot to the standing pose in the first step
    myMovements.standingPose(joints=NAO6_joints)

    # NAO6_joints[myJoints.joint_names.index('LHipYawPitch')].setPosition(15*3.1416/180)
    # NAO6_joints[myJoints.joint_names.index('LKneePitch')].setPosition(25*3.1416/180)

    # # Read current joint positions from sensors
    # current_angles = myMovements.getCurrentAngles(NAO6_sensors=NAO6_sensors)
    #
    # # Get the walking gait for the current step
    # # gait = myMovements.getWalkingGait(step_time=0.5)  # Example step time of 0.5 seconds
    # gait = myMovements.getWalkingGait(step_time=0.5)
    #
    # # Update the initial state for MPC
    # q = cp.Variable((myMovements.num_walking_joints, myControlLib.N + 1))  # Joint positions over the horizon
    # dq = cp.Variable((myMovements.num_walking_joints, myControlLib.N))  # Joint velocities (control inputs)
    #
    # # Define and solve the MPC problem for walking
    # problem = myControlLib.defineWalkingMpc(q0=current_angles[12:],
    #                                         gait=gait,
    #                                         q=q,
    #                                         dq=dq,
    #                                         N=myControlLib.N,
    #                                         step_time=0.5)
    # problem.solve()
    #
    # # Get the first control input (dq[:, 0]) to apply
    # control_input = dq[:, 0].value
    #
    # print(f'Current Angles: {current_angles}')
    # print(f'Control Input: {control_input}')
    #
    # # Apply control inputs to the joints in Webots
    # for i in range(12, len(NAO6_joints)):
    #
    #     NAO6_joints[i].setPosition(current_angles[i] + control_input[i-12]*600)  # Apply the control to joints
    #
    # # Stop after 1 minute
    # current_step += 1
    # print(f'Current step is: {current_step}')
    # if current_step >= total_steps:
    #     break

print("Simulation completed after 10 minutes.")
