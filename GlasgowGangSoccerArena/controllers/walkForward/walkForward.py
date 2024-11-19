# Copyright 1996-2023 Cyberbotics Ltd.
# Licensed under the Apache License, Version 2.0

from controller import Robot, Motion

class Nao(Robot):
    def __init__(self):
        super().__init__()
        self.timeStep = int(self.getBasicTimeStep())
        self.forwards = Motion('D:\Robotics&AI\GlasgowGangRobot\GlasgowGangSoccerArena\controllers\SupervisorPositionController\motions\Forwards50.motion')
        self.currentlyPlaying = None

    def startMotion(self, motion):
        # Stop current motion if active, then start the new motion
        if self.currentlyPlaying:
            self.currentlyPlaying.stop()
        motion.play()
        self.currentlyPlaying = motion

    def run(self):
        # Start forward motion and set it to loop
        self.startMotion(self.forwards)
        self.forwards.setLoop(True)
        
        # Define the duration (1 minute)
        duration_seconds = 60
        start_time = self.getTime()

        # Loop to walk forward for 1 minute
        while self.step(self.timeStep) != -1:
            elapsed_time = self.getTime() - start_time
            
            # Stop after 1 minute
            if elapsed_time >= duration_seconds:
                self.forwards.stop()
                break

# Instantiate and run the robot
robot = Nao()
robot.run()
