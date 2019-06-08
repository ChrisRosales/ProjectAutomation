import glob
import sys
import os
from config import path


def delete():
    directory = path
    os.removedirs(directory + str(sys.argv[1]))
    print("Succesfully deleted project {}".format(sys.argv[1]))


if __name__ == "__main__":
    delete()
