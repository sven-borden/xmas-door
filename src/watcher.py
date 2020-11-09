from gpiozero import MotionSensor

pir = MotionSensor(4)


def trigger():
    print('hi')


def start_watch():
    """
    Infinite loop that waits for the PIR to trigger.
    Once triggered, call a sound.
    """
    pir.when_motion = trigger()


if __name__ == "__main__":
    start_watch()
