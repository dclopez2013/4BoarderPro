import sys
from gooey import Gooey,GooeyParser
import argparse
import json
import os
import downloader as dl
from downloader import p4

@Gooey(optional_cols=2, program_name="Instagram JSON Parser")
def __main__():


    settings_msg = '4Chan  Board Parser'
    parser = GooeyParser(description=settings_msg)

    parser.add_argument('--verbose', help='be verbose', dest='verbose',
                        action='store_true', default=False)

    subs = parser.add_subparsers(help='commands', dest='command')
    thread_parser = subs.add_parser('FromThreads', help='JSON Messages helps parse instagram messages stored in JSON')

    thread_parser.add_argument("--board", help="Exact board to download ie 'gif' ")
    thread_parser.add_argument("--thread", help="Exact thread id to access ie 15534266")
    thread_parser.add_argument('-saveLocation', help="Select where you want to save the files", widget="DirChooser")

    # ------------------------------------------------#

    urlFile_parser = subs.add_parser('FromFile', help='Reads and downloads files from urls in txt file')

    urlFile_parser.add_argument('--TxtFileLocation', help="name of the JSON Comment file to process", widget="FileChooser")
    urlFile_parser.add_argument('-saveLocation', help="Select where you want to save the files", widget="DirChooser")
    urlFile_parser.add_argument("--dirName", help="Name to give created folder ")


    args = parser.parse_args()

    command = args.command

    #parses command chosen

    print("Parsing command : "+ command+"\n")
    commandParser(command, args)
    #print(args)
   # print(args)
    #print(argsa)



def commandParser(command, args):

    if "FromFile" in command:

        if args.TxtFileLocation and args.saveLocation:
            fileLocation = args.TxtFileLocation
            saveLoc = args.saveLocation
            dirName = args.dirName



    elif "FromThreads" in command:
        if args.board and args.thread and args.saveLocation:
            board = args.board
            thread = args.thread
            saveLoc = args.saveLocation
            try:
                dl.downloadOneThread(thread, board,saveLoc)
            except Exception as e:
                print(str(e))
        else:

            print("No fields can be blank")



if __name__ == '__main__':

    __main__()