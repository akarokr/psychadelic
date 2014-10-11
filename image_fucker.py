#!/usr/bin/env python
"""Usage:
          image_fucker.py --file=image_file [--amount=10]
"""
import random
import sys
import docopt
import os


def check_image_file(image_path):
    image_path = os.path.expanduser(image_path)
    if not os.path.isfile(image_path):
        print "There is no such file on the disk, you stupid cunt!\n"
    return image_path


def teleport(file_data):
    entry = random.randint(2500, len(file_data))  # No touching of the precious headers, yo
    end = entry + random.randint(0, len(file_data) - entry)

    return entry, end


def hack_and_slash(file_data):
    start_point, end_point = teleport(file_data)
    section = file_data[start_point:end_point]
    repeated = ''

    for i in range(1, random.randint(1, 8)):
        repeated += section

    new_start_point, new_end_point = teleport(file_data)
    file_data = file_data[:new_start_point] + repeated + file_data[new_end_point:]
    return file_data


def mess_up_everything(local_image, micrograms=5):
    reader = open(local_image, 'r')
    file_data = reader.read()
    reader.close()

    for i in range(1, micrograms):
        file_data = hack_and_slash(file_data)
    name = local_image.split(".")[0]
    ext = local_image.split(".")[1]
    glitched = name + "_psych." + ext
    writer = open(glitched, 'w')
    writer.write(file_data)
    writer.close

    return glitched


if __name__ == '__main__':
    arguments = docopt.docopt(__doc__)
    if arguments.get("--file") is None:
        print "Provide an original image, you stupid cunt!\n"
        sys.exit(1)
    if arguments.get("--amount"):
        try:
            micrograms = int(arguments.get("--amount"))
        except ValueError:
            print "You didn't provide a valid integer value, falling back to 5 glitchyness."
            micrograms = 5
    else:
        micrograms = 5
    original_file = check_image_file(arguments.get("--file"))
    image_glitch_file = mess_up_everything(original_file, micrograms)

    print "Your image is fucked, and can be found at %s" % image_glitch_file