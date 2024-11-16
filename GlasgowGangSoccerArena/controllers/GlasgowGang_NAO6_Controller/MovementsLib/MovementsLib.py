from ConstantsLib import ConstantsLib
import numpy as np

class movements():

    def __init__(cls):
        """

        """

        cls.hello = ''
        cls.myConstantsLib = ConstantsLib

        cls.num_walking_joints = 12

        # Actual joint limits for NAO6 robot
        cls.walking_joint_min = np.array([
            -1.145303, -0.379472, -1.535889, -0.092346, -1.189516, -0.397880,  # Left leg
            -1.145303, -0.379472, -1.535889, -0.092346, -1.189516, -0.397880  # Right leg
        ])

        cls.walking_joint_max = np.array([
            0.740810, 0.790477, 0.484090, 2.112528, 0.922747, 0.769001,  # Left leg
            0.740810, 0.790477, 0.484090, 2.112528, 0.922747, 0.769001  # Right leg
        ])



    def standingPose(self, joints):
        """
        Created by: Misael Rivera
        Created on: 22/Oct/2024

        Modified by: -
        Modified on: -

        This will contain all the joints information and constraints

        """

        standing_pose_angles = self.myConstantsLib.joints().standing_pose_angles

        for i, joint in enumerate(joints):
            joint.setPosition(standing_pose_angles[i])

    def getCurrentAngles(self, NAO6_sensors):

        """
        Created by: Misael Rivera
        Created on: 22/Oct/2024

        Modified by: -
        Modified on: -

        :param: NAO6_sensors:

        """

        current_angles = []

        for each_sensor in NAO6_sensors:

            current_angles.append(each_sensor.getValue())

        current_angles = np.array(current_angles)

        return current_angles


    # Define the walking gait (step patterns, leg movements)
    def getWalkingGait(self, step_time, stride_length=0.05):
        """
        Created by: Misael Rivera
        Created on: 22/Oct/2024

        Modified by: -
        Modified on: -


        Define the target joint positions for walking.
        Adjust `stride_length` and `step_time` for different walking speeds.
        """

        # Initialize gait pattern for each joint (2 phases: left leg forward, right leg forward)
        gait = np.zeros((self.num_walking_joints, 2))

        # Time scaling for walking speed
        step_time_scaled = step_time * speed

        # Phase 1: Left leg forward, right leg back
        gait[2, 0] = -stride_length  # LHipPitch forward
        gait[3, 0] = 0.5  # LKneePitch bent (for foot clearance)
        gait[4, 0] = -step_height  # LAnklePitch lifting foot

        gait[8, 0] = stride_length  # RHipPitch backward
        gait[9, 0] = -0.5  # RKneePitch straighten
        gait[10, 0] = step_height  # RAnklePitch lowering foot

        # Phase 2: Right leg forward, left leg back
        gait[2, 1] = stride_length  # LHipPitch backward
        gait[3, 1] = -0.5  # LKneePitch straighten
        gait[4, 1] = step_height  # LAnklePitch lowering foot

        gait[8, 1] = -stride_length  # RHipPitch forward
        gait[9, 1] = 0.5  # RKneePitch bent (for foot clearance)
        gait[10, 1] = -step_height  # RAnklePitch lifting foot

        # Optional: Side-to-side hip roll for balance
        gait[1, 0] = 0.05  # LHipRoll: Slight outward movement
        gait[7, 0] = -0.05  # RHipRoll: Slight outward movement

        gait[1, 1] = -0.05  # LHipRoll: Return to neutral
        gait[7, 1] = 0.05  # RHipRoll: Return to neutral

        return gait, step_time_scaled


    def get_walking_gait(self, step_time, dt):

        # Parameters to define the gait
        step_length = 0.12  # Increase this value for longer steps
        step_frequency = 2.2  # Increase this value for faster stepping

        # Calculate the time for each step
        step_duration = 1.0 / step_frequency

        gait = []
        # Generate gait pattern
        for t in range(int(step_duration / dt)):
            # Adjust joint positions for each step, increase movement
            gait.append((step_length, 0.0))  # Example (forward movement, sideways movement)

        return gait
