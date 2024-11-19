from controller import Supervisor, Motion

# Initialize the Supervisor
supervisor = Supervisor()
time_step = int(supervisor.getBasicTimeStep())

# Retrieve the ball's node
ball_name = "BALL"
ball = supervisor.getFromDef(ball_name)

# Retrieve the supervisor's own position
supervisor_node = supervisor.getSelf()
translation_field = supervisor_node.getField("translation")

# Load motion files
step_right = Motion("D:\Robotics&AI\GlasgowGangRobot\GlasgowGangSoccerArena\controllers\SupervisorPositionController\motions\SideStepRight.motion")
step_left = Motion("D:\Robotics&AI\GlasgowGangRobot\GlasgowGangSoccerArena\controllers\SupervisorPositionController\motions\SideStepLeft.motion")
shoot = Motion("D:\Robotics&AI\GlasgowGangRobot\GlasgowGangSoccerArena\controllers\SupervisorPositionController\motions\Shoot.motion")

# Define movement parameters
alignment_threshold_y = 0.1  # Minimum Y distance to trigger movement
alignment_threshold_x = 0.25  # X distance to trigger shooting
step_size = 0.1  # Approximate step size per motion (adjust based on motion file)

# Helper function to play a motion
def play_motion(motion):
    motion.play()
    while not motion.isOver():
        supervisor.step(time_step)

# Main loop
while supervisor.step(time_step) != -1:
    # Get the ball's position
    ball_position = ball.getField("translation").getSFVec3f()
    ball_x, ball_y = ball_position[0], ball_position[1]

    # Get the supervisor's current position
    supervisor_position = translation_field.getSFVec3f()
    supervisor_x, supervisor_y = supervisor_position[0], supervisor_position[1]

    # Calculate position differences
    position_diff_y = ball_y - supervisor_y
    position_diff_x = abs(ball_x) - abs(supervisor_x)

    # Align supervisor's position on the Y-axis using motion files
    if abs(position_diff_y) > alignment_threshold_y:
        if position_diff_y > 0:
            # Ball is above the supervisor's position, step right
            play_motion(step_left)
            print(f"Stepped right to align closer to ball at Y={ball_y:.2f}.")
        else:
            # Ball is below the supervisor's position, step left
            play_motion(step_right)
            print(f"Stepped left to align closer to ball at Y={ball_y:.2f}.")
    elif abs(position_diff_x) <= alignment_threshold_x:
        # Perform shoot motion if X difference is small and Y is aligned
        print(f"Aligned on Y and within X threshold, performing shoot motion!")
        play_motion(shoot)

    print()  # Blank line for readability
