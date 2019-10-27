import cv2,time


def check_video_frame_data():
    video=cv2.VideoCapture(0)
    check,frame = video.read()
    print(check)
    print(frame)
    video.release()
    return

def watch_video_stream_data():
    video=cv2.VideoCapture(0)

    a = 0
    while True:
        a+=1
        check,frame = video.read()
        print(check)
        print(frame)
        # Convert to grayscale
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('Capturing',gray)

        # Play stream
        key = cv2.waitKey(1)
        if key== ord('q'):
            break

    video.release()
    cv2.destroyAllWindows
    return
