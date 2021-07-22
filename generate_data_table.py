import os
import sys



def main():
    argc = len(sys.argv)
    if (argc != 2):
        print("Usage: python3 generate_data_table.py <frame file>")
        exit()

    files = [x for x in os.listdir(os.getcwd()) if (x.endswith("_Segments.txt"))]
    for fileName in files:
        file = open(fileName, "r").read()
        video_name = fileName.split("_Segments.txt")[0]
        sign_seqs = file.split("\n\n")[0].split("\n")[1:]
        non_sign_seqs = file.split("\n\n")[1].split("\n")[1:-1]
        
        "{}_frame_{}.jpg".format(video_name, count)


if __name__ == "__main__":
    main()
