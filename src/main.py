import os
import logging

from LABA2.src.power import ls
from LABA2.src.power import cd
from LABA2.src.power import cat
from LABA2.src.power import cp
from LABA2.src.power import mv
from LABA2.src.power import rm
from LABA2.src.power import zip
from LABA2.src.power import unzip
from LABA2.src.power import tar
from LABA2.src.power import untar
from LABA2.src.power import grep
from LABA2.src.logg import make_logger

def main() -> None:
    """ Точкой входа в приложение
    return: Данная функция ничего не возвращает"""
    logger = make_logger()
    print("Мини оболочка  на python. Введите break для выхода.")
    while True:
        input_ = str(input())
        command,arg,arg2,arg3,arg4 = parser(input_)
        
        file_path = os.getcwd()
        print(file_path)
        try:
            if command == "break":
                logging.info("Завершение программы")
                break
            if(command == "ls"):
                if(arg == "-l"):
                    if(arg2 != ""):
                        ls(arg,arg2)
                    else:
                        ls(arg,".")
                else:
                    if (arg != ""):
                        ls(1,arg)
                    else:
                        ls(1, ".")
            elif (command == "cd"):
                cd(arg)
            elif (command == "cat"):
                cat(arg)
            elif (command == "cp"):
                if arg == "" or arg2 == "":
                    print("Требуется минимум 2 аргумента")
                else:
                    if(arg == "-r"):
                        cp(arg,arg2,arg3)
                    else:
                        cp(0,arg,arg2)
            elif (command == "rm"):
                print("Are you sure you want to delete? y/n")
                answer = str(input())
                if answer == "y":
                    if arg:
                        rm(arg,arg2)
                    else:
                        rm(1,arg2)
                else:
                    print(" ")
            elif (command == "mv"):
                mv(arg,arg2)
            elif (command == "zip"):
                zip(arg,arg2)
            elif (command == "unzip"):
                unzip(arg)
            elif (command == "tar"):
                tar(arg,arg2)
            elif (command == "untar"):
                untar(arg)
            elif (command == "grep"):
                if arg == "-r" or arg == "-i":
                    grep(arg,arg2,arg3)
                else:
                    grep(1,arg2,arg3)
        except Exception as e:
            logging.error({e})
            print(f"{e}")
if __name__ == "__main__":
    main()
