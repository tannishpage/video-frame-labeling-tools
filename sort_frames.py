import sys
import os

def main():
    if (len(sys.argv) != 3):
        print("Usage python3 sort_frames.py <sort_file> <video_name>")
        sys.exit()
    f = open(sys.argv[1], 'r')
    x = f.read()
    sign_seqs = x.split("\n\n")[0].split("\n")[1:]
    non_sign_seqs = x.split("\n\n")[1].split("\n")[1:-1]
    video_name = sys.argv[2]
    os.chdir(video_name)
    os.mkdir("{}_sign_seq".format(video_name))
    os.mkdir("{}_non_sign_seq".format(video_name))

    for i, sign_seq in enumerate(sign_seqs):
        start = int(sign_seq.split(":")[0])
        end = int(sign_seq.split(":")[1])
        copy_dir = "./{}_sign_seq/sign_seq_{}".format(video_name, i+1)
        os.mkdir(copy_dir)
        for x in range(start, end+1):
            os.system("mv {}.mkv_frame_{}.jpg {}".format(video_name, x, copy_dir))

    for i, non_sign_seq in enumerate(non_sign_seqs):
        start = int(non_sign_seq.split(":")[0])
        end = int(non_sign_seq.split(":")[1])
        copy_dir = "./{}_non_sign_seq/non_sign_seq_{}".format(video_name, i+1)
        os.mkdir(copy_dir)
        for x in range(start, end+1):
            os.system("mv {}.mkv_frame_{}.jpg {}".format(video_name, x, copy_dir))

if __name__ == "__main__":
    main()
