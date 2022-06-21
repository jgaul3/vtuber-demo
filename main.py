import cv2
import sounddevice as sd
import numpy as np


level = 0


def update_sound(indata, outdata, frames, time, status):
    global level
    level = np.linalg.norm(indata)*10


def main():
    # define a video capture object
    vid = cv2.VideoCapture(0)

    state = 0
    with sd.Stream(callback=update_sound):
        while True:
            # Capture the video frame
            # by frame
            ret, frame = vid.read()

            if level > 3:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                print('asdf')
            else:
                print("")

            # Display the resulting frame
            cv2.imshow('frame', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    # Destroy all the windows
    cv2.destroyAllWindows()
    # After the loop release the cap object
    vid.release()


if __name__ == "__main__":
    main()
