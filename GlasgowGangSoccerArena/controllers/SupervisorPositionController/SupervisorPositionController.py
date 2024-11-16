from controller import Supervisor

# Initialize the Supervisor
supervisor = Supervisor()
time_step = int(supervisor.getBasicTimeStep())

# List of robot DEF names in the simulation
robot_names = ["ATTACKER_1",
               "DEFENDER_1", 
               "DEFENDER_2", 
               "GOALKEEPER_1", 
               "BALL"]  # Add your robot DEF names here

# Retrieve each robot's node using its DEF name
robots = [supervisor.getFromDef(name) for name in robot_names]

# Define the update interval (5 seconds)
update_interval = 1000
last_update_time = 0

# Main loop
while supervisor.step(time_step) != -1:
    # Check if 5 seconds have passed
    current_time = supervisor.getTime() * 1000  # Convert to milliseconds
    if current_time - last_update_time >= update_interval:
        last_update_time = current_time
        print(f"Time: {supervisor.getTime():.2f} seconds")

        # Print the position of each robot
        for robot, name in zip(robots, robot_names):
            if robot is not None:
                # Get the robot's position field
                position = robot.getField("translation").getSFVec3f()
                print(f"{name} position: x={position[0]:.2f}, y={position[1]:.2f}, z={position[2]:.2f}")
            else:
                print(f"Error: Could not find robot with DEF name '{name}'")

        print()  # Blank line for readability
