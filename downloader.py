
from __future__ import print_function

import basc_py4chan
import json
import requests
import os

def downloadEmAll(board):
    if not (os.path.exists("images")):
        print("output directeory doesnt exist")
        print("creating output folder")
        os.mkdir("images")
        print("Output folders created!")
    else:
        print("output directory already exists")
    tBoard = board
    tID = tBoard.get_all_thread_ids()

    for id in tID:
        print("Downloading from board: ",id)
        print(id)
        downloadFromOneThread(id, tBoard)


def downloadFromOneThread(id, board):

    if not (os.path.exists("images")):
        print("output directeory doesnt exist")
        print("creating output folder")
        os.mkdir("images")
        print("Output folders created!")
    else:
        print("output directory already exists")


    testThread = board.get_thread(id)
    fileUrl = []
    fileUrlName = []
    if testThread:
        print("found thread")
    else:
        print("thread not found")

    for f in testThread.file_objects():
        r = requests.get(f.file_url)
        with open("C:\Users\dclop\PycharmProjects\Boarder\images\\" + f.filename, "wb") as myFile:
            for chunk in r.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    myFile.write(chunk)



