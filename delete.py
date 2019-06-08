import glob
import sys
import os
from config import path


def delete():
    path = path
    os.removedirs(path + str(sys.argv[1]))
    print("Succesfully deleted project {}".format(sys.argv[1]))


if __name__ == "__main__":
    delete()
