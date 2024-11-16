from controller import Robot


class joints():

    def __init__(cls):
        """
        Created by: Misael Rivera
        Created on: 22/Oct/2024

        Modified by: -
        Modified on: -

        This will contain all the joints information and constraints

        """

        cls.joints = []
        cls.sensors = []

        # Define the standing pose joint angles (approximate)
        # These values may need fine-tuning depending on the exact standing posture of the NAO6 in Webots.
        cls.standing_pose_angles = [
            0.0,  # HeadYaw
            0.0,  # HeadPitch
            1.5,  # LShoulderPitch (arms down)
            0.0,  # LShoulderRoll
            0.0,  # LElbowYaw
            0.0,  # LElbowRoll
            0.0,  # LWristYaw
            1.5,  # RShoulderPitch (arms down)
            0.0,  # RShoulderRoll
            0.0,  # RElbowYaw
            0.0,  # RElbowRoll
            0.0,  # RWristYaw
            0.0,  # LHipYawPitch (standing)
            0.0,  # LHipRoll
            0,  # LHipPitch (slight backward bend to maintain balance)
            0.0,  # LKneePitch (bent knees for standing)
            0,  # LAnklePitch (balances the knee bend)
            0.0,  # LAnkleRoll
            0.0,  # RHipYawPitch
            0.0,  # RHipRoll
            0,  # RHipPitch
            0.0,  # RKneePitch
            0,  # RAnklePitch
            0.0  # RAnkleRoll
        ]

        cls.joint_names = [
            'HeadYaw', 'HeadPitch',  # Head Joints
            'LShoulderPitch', 'LShoulderRoll', 'LElbowYaw', 'LElbowRoll', 'LWristYaw',  # Left Arm Joints
            'RShoulderPitch', 'RShoulderRoll', 'RElbowYaw', 'RElbowRoll', 'RWristYaw',  # Right Arm Joints
            'LHipYawPitch', 'LHipRoll', 'LHipPitch', 'LKneePitch', 'LAnklePitch', 'LAnkleRoll',  # Left Leg Joints
            'RHipYawPitch', 'RHipRoll', 'RHipPitch', 'RKneePitch', 'RAnklePitch', 'RAnkleRoll'  # Right Leg Joints
        ]

        cls.joint_limits = {
            "HeadYaw": [-2.0857, 2.0857],
            "HeadPitch": [-0.6720, 0.5149],
            "LShoulderPitch": [-2.0857, 2.0857],
            "LShoulderRoll": [-0.3142, 1.3265],
            "LElbowYaw": [-2.0857, 2.0857],
            "LElbowRoll": [-1.5446, -0.0349],
            "LWristYaw": [-1.8238, 1.8238],
            "LHand": [0.0, 1.0],
            "RShoulderPitch": [-2.0857, 2.0857],
            "RShoulderRoll": [-1.3265, 0.3142],
            "RElbowYaw": [-2.0857, 2.0857],
            "RElbowRoll": [0.0349, 1.5446],
            "RWristYaw": [-1.8238, 1.8238],
            "RHand": [0.0, 1.0],
            "LHipYawPitch": [-1.1453, 0.7408],
            "LHipRoll": [-0.3794, 0.7904],
            "LHipPitch": [-1.5359, 0.4840],
            "LKneePitch": [-0.0923, 2.1125],
            "LAnklePitch": [-1.1895, 0.9227],
            "LAnkleRoll": [-0.3978, 0.7690],
            "RHipYawPitch": [-1.1453, 0.7408],
            "RHipRoll": [-0.7904, 0.3794],
            "RHipPitch": [-1.5359, 0.4840],
            "RKneePitch": [-0.0923, 2.1125],
            "RAnklePitch": [-1.1895, 0.9227],
            "RAnkleRoll": [-0.7690, 0.3978],
            "TorsoPitch": [-1.0, 1.0]  # Torso might only have 1 DoF
        }

    def createNAO6Joints(self, NAO6_robot):

        """
        Created by: Misael Rivera
        Created on: 22/Oct/2024

        Modified by: -
        Modified on: -

        This will contain all the joints information and constraints

        :param NAO6_robot:
        :return:
        """

        for each_joint in self.joint_names:

            self.joints.append(NAO6_robot.getDevice(each_joint))


        return self.joints

    def createNAO6Sensors(self, joints, timestep):

        """
        Created by: Misael Rivera
        Created on: 22/Oct/2024

        Modified by: -
        Modified on: -

        This will contain all the joints information and constraints

        :param NAO6_robot:
        :return:
        """

        for each_joint in joints:

            self.sensors.append(each_joint.getPositionSensor())

        for sensor in self.sensors:
            sensor.enable(timestep)

        return self.sensors