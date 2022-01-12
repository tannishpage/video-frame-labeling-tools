"""
This script is intended to be used to convert data of the form

    Sign_Seg:
    0:11822

    Non_Sign_Seg:
    11823:12362

where the numbers represent start_frame:end_frame

to the form

<video_id> <frame_id> <label>

---------------------------------
Labels:

sign = 1
non_sign = 0
---------------------------------

Make sure the file names are of the form:

<vidoe_id>.txt or <video_id>_Segments.txt
"""

import os
import sys

def convert_seqs_to_tuples(seqs, label):
    tuple_seq = []
    for seq in seqs:
        start, end = tuple(seq.split(":"))
        tuple_seq.append(tuple((int(start), int(end), label)))
    return tuple_seq

def convert_file(file_name):
    if file_name.endswith("_Segments.txt"):
        video_id = file_name.split("_Segments.txt")[0]
    elif file_name.endswith(".txt"):
        video_id = file_name.split(".txt")[0]
    else:
        print("File name {} not in correct format, couldn't determin video id".format(file_name))
        return ""

    file = open(file_name, "r").read()
    sign_seqs = convert_seqs_to_tuples(file.split("\n\n")[0].split("\n")[1:], 1)
    non_sign_seqs = convert_seqs_to_tuples(file.split("\n\n")[1].split("\n")[1:-1], 0)
    seqs = sorted(sign_seqs + non_sign_seqs)

    new_file = []
    for seq in seqs:
        new_file += ["{} {} {}\n".format(video_id, i, seq[2]) for i in range(seq[0], seq[1]+1)]

    return "".join(new_file)



def main():
    data_table_file_name = os.path.join(os.getcwd(), "data_table.txt")
    name_count = -1
    argc = len(sys.argv)
    if (argc != 2):
        print("Usage: python3 generate_data_table.py <dir of labelling files>")
        exit(1)

    if not (os.path.exists(sys.argv[1])):
        print("Path {} does not exist".format(sys.argv[1]))
        exit(1)

    if os.path.isfile(sys.argv[1]):
        line = convert_file(sys.argv[1])
        file = open("single_file.txt", 'w')
        file.write(line)
        file.close()
        exit(0)
    else:
        while os.path.exists(data_table_file_name):
            name_count += 1
            data_table_file_name = os.path.join(os.getcwd(), "data_table_{}.txt".format(name_count))
        data_table_file = open(data_table_file_name, "w")
        file_names = [x for x in os.listdir(sys.argv[1])]
        os.chdir(sys.argv[1])
        for file_name in file_names:
            print("Converting File {}....".format(file_name), end='')
            line = convert_file(file_name)
            if line == "":
                continue
            data_table_file.write(line)
            print("Done")

        data_table_file.close()


if __name__ == "__main__":
    main()
