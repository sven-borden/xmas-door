import os
import random
from signal import pause

import pygame
from gpiozero import MotionSensor
from pygame import mixer

pir = MotionSensor(4)
mixer.init()


sounds = {
    "doorbell": "src/sounds/Christmas-doorbell-melody.wav",
    "doorbell": "src/sounds/Christmas-doorbell-melody.wav",
    "doorbell": "src/sounds/Christmas-doorbell-melody.wav",
    "doorbell": "src/sounds/Christmas-doorbell-melody.wav",
    "doorbell": "src/sounds/Christmas-doorbell-melody.wav"
}


def play_sound(path, absolut_path='/home/pi/xmas-door/'):
    """
    Function that will play a sound on the raspberry pi

    Arguments
    ---------
    path : str
        The relative path from the root of this repository

    Raises
    ------
    On pygame error raise SystemExit
    """
    sound = mixer.Sound(os.path.join(absolut_path, path))
    sound.set_volume(1.0)
    try:
        sound.play()
    except pygame.error as message:
        raise SystemExit(message)


def someone_crossed():
    """
    Callback when someone entered or went out and was detected
    """
    play_sound(random.choice(list(sounds.values())))


def start_watch():
    """
    Infinite loop that waits for the PIR to trigger.
    Once triggered, call a sound.
    """
    pir.when_motion = someone_crossed
    pause()


if __name__ == "__main__":
    start_watch()
