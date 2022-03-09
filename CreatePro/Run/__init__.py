"""
Run CreatePro
"""
import os
import sys


class Execute:
    def __init__(self):
        pass

    @staticmethod
    def main():
        if 'CreateInfo' in os.listdir(os.path.split(sys.argv[0])[0]):
            with open('CreateInfo') as info:
                print(info.read())
        else:
            print('CreateInfo is missing, stop')
            print(__file__)


if __name__ == '__main__':
    raise ImportError("'Can't run")
else:
    Execute.main()
