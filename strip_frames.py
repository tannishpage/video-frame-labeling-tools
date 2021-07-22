import cv2
import os
import multiprocessing

videos = [vid for vid in os.listdir(os.getcwd()) if vid.endswith(".mp4") or vid.endswith(".mkv")]
lent = len(videos)

def strip_f(vids, id):
    length = len(vids)
    for i, vid in enumerate(vids):
        cap = cv2.VideoCapture(vid)
        count = 0
        os.mkdir(vid[0:-4])
        os.chdir(vid[0:-4])
        print("{}: [{}/{}] Stripping frames for {}...".format(id, i+1, length, vid), flush=True)
        while True:
            ret, frame = cap.read()
            count += 1
            if (count % 1) == 0:
                if ret == True:
                    cv2.imwrite("{}_frame_{}.jpg".format(vid, count), frame)
                    #cv2.imshow('Frame',frame)
                    if cv2.waitKey(25) & 0xFF == ord('q'):
                        break
                else:
                    break
        os.chdir("../")
    else:
        print("{}: -------------- Finished My part --------------".format(id))

num_splits = 20
start = 0.0
end = lent / num_splits
for x in range(0, num_splits):
    multiprocessing.Process(target=strip_f, args=(videos[int(start):int(end)], x,)).start()
    start = end
    end += lent / num_splits
