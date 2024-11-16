from controller import Robot
import numpy as np
import cvxpy as cp
from MovementsLib.MovementsLib import movements

class ModelPredictiveControl():

    def __init__(cls, timestep):
        """
        Created by: Misael Rivera
        Created on: 22/Oct/2024

        Modified by: -
        Modified on: -

        This will contain all the joints information and constraints

        :param NAO6_robot:
        :return:
        """

        # MPC horizon and time step
        cls.N = 10  # Prediction horizon
        cls.dt = timestep / 1000.0  # Convert timestep to seconds


    # Define MPC optimization problem
    def defineWalkingMpc(self, q0, gait, q, dq, N, step_time):

        """
        Created by: Misael Rivera
        Created on: 22/Oct/2024

        Modified by: -
        Modified on: -

        This will contain all the joints information and constraints

        :param q0:
        :param gait:
        :param step_time:
        :return:
        """

        cost = 0
        constraints = [q[:, 0] == q0]

        for k in range(N):
            # Cost function: minimize deviation from gait and control effort
            cost += cp.sum_squares(q[:, k + 1] - gait[:, k % 2])  # Penalize deviation from the gait pattern
            cost += cp.sum_squares(dq[:, k])  # Minimize control effort

            # Dynamics: next state based on current state and control input
            constraints += [q[:, k + 1] == q[:, k] + dq[:, k] * self.dt]

            # Enforce joint limits
            constraints += [movements().walking_joint_min <= q[:, k + 1], q[:, k + 1] <= movements().walking_joint_max]

        problem = cp.Problem(cp.Minimize(cost), constraints)
        return problem