
from __future__ import print_function
import basc_py4chan as p4
import time
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


def downloadFromOneThread(id, board, saveLoc):

    if not (os.path.exists(saveLoc)):
        print("output directory doesnt exist")
        print("creating output folder")
        os.mkdir(saveLoc)
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
        with open(saveLoc +"\\"+ f.filename, "wb") as myFile:
            for chunk in r.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    myFile.write(chunk)
        myFile.close()


def downloadOneThread(id, board,dir):

    fDir = dir +"\\"+id

    if not (os.path.exists(fDir)):
        print("output directory doesnt exist")
        print("creating output folder")
        os.mkdir(fDir)
        print("Output folders created!")
    else:
        print("output directory already exists")

    tBoard=p4.Board(str(board))

    if not tBoard:
        print("Board Not Found")
        return 0
    else:
        print(tBoard.title)
        testThread = tBoard.get_thread(id)
        fileUrl = []
        fileUrlName = []
        if testThread:
            print("found thread")
        else:
            print("thread not found")

        end = testThread.file_objects().__sizeof__()
        print(end," file objects found to be downloaded")
        files = testThread.file_objects()
        fileNameList = None
        for f in testThread.file_objects():

           # fileNameList.append(f.file_url)

            if os.path.exists(fDir+"\\"+f.filename):
                print("File exists")
                time.sleep(1)

            else:
                r = requests.get(f.file_url)
                print("Attempting to Download ", f.filename)
                print("Downloading to >>" + fDir)


                print("file doesnt exist. Downloading")
                with open(fDir+"\\"+f.filename, "wb") as myFile:
                    for chunk in r.iter_content(chunk_size=1024 * 1024):
                        if chunk:
                            myFile.write(chunk)

                myFile.close()
                print("File Download Complete")

                time.sleep(1)

def downloadRaw(urls,dirName,loc):

    fDir = loc +"\\"+dirName
    count =len(urls)
    if not (os.path.exists(fDir)):
        print("output directory doesnt exist")
        print("creating output folder")
        os.mkdir(fDir)
        print("Output folders created!")
    else:
        print("output directory already exists")


    for x in range(count):
    # for f in urls:

           # fileNameList.append(f.file_url)

        if os.path.exists(fDir+"\\"+str(x)+".jpg"):
                print("File exists")
                time.sleep(1)

        else:
            try:
                r = requests.get(urls[x])
                print("Attempting to Download ", urls[x])
                print("Downloading to >>" + fDir)


                print("file doesnt exist. Downloading")
                with open(fDir+"\\"+urls[x], "wb") as myFile:
                    for chunk in r.iter_content(chunk_size=1024 * 1024):
                        if chunk:
                            myFile.write(chunk)

                myFile.close()
                print("File Download Complete")

                time.sleep(1)
            except Exception as e:
                print(e)

def dlTextLink(url,loc,dirName,count):

    fDir = loc +"\\"+dirName
    if not (os.path.exists(fDir)):
        print("output directory doesnt exist")
        print("creating output folder")
        os.mkdir(fDir)
        print("Output folders created!")
    else:
        print("output directory already exists")


    r = requests.get(url)
    print("Attempting to Download ", count)
    print("Downloading to >>" + fDir)

    print("file doesnt exist. Downloading")
    with open(fDir + "\\" +count+".jpg" , "wb") as myFile:
        for chunk in r.iter_content(chunk_size=1024 * 1024):
            if chunk:
                myFile.write(chunk)

    myFile.close()
    print("File Download Complete")

    time.sleep(1)