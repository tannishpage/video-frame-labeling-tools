import cv2
import os
import sys


def main():
    argc = len(sys.argv)
    if (argc != 2):
        print("Useage: python3 frame_segment_maker.py <video_name>")
        exit()

    cap = cv2.VideoCapture(sys.argv[1])
    read_stat, img = cap.read()
    while read_stat:
        read_stat, img = cap.read()
        cv2.imshow("frame", img)
        if (cv2.waitKey(25)):
            while True:
                if (cv2.waitKey(25)):
                    break

if __name__ == "__main__":
    main()
