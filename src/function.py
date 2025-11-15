import os
import datetime
import logging
import shutil
from pathlib import Path

def parser(input_):
    words = input_.split()
    command = words[0] if words else ""
    arg = words[1] if len(words) >  1 else ""
    arg2 = words[2] if len(words) > 2 else ""
    arg3 = words[3] if len(words) > 3 else ""
    arg4 = words[4] if len(words) > 4 else ""

    return command,arg,arg2,arg3,arg4
    
def ls(arg,path_):
    """
    Отображение списка файлов и директорий в текущем каталоге
    :param arg: -l для более подробного отобрадения(дата,права и т.д)
    :param path_:
    :return:Просто выводит содержимое
    """
    try:
        path_ = os.path.abspath(path_)
        if not os.path.exists(path_):
            raise FileNotFoundError(f"Каталог не существует: {path_}")
        files_in_directory = os.listdir(path = path_)
        if arg == "-l":
            print(f"Содержимое каталога:")
            for item in files_in_directory:
                if item[0] == ".":
                    continue
                path = os.path.join(path_, item)
                stat = os.stat(path)
                permissions = '-'
                size = stat.st_size
                mtime = datetime.datetime.fromtimestamp(stat.st_mtime)
                mtime_str = mtime.strftime("%Y-%m-%d %H:%M")
                item_type = 'd' if os.path.isdir(path) else '-'
                print(f"{item_type}{permissions} {size:>8} {mtime_str} {item}")
            logging.info(f"ls -l{arg, path_}.")
        else:
            for item in files_in_directory:
                if item[0] == ".":
                    continue
                else:
                    print(item)
            logging.info(f"ls {path_}.")
    except Exception as e:
        logging.error({e})
        return False,print(f"{e}")

def cd(path_):
    """
    Изменение текущего каталога
    :param path_:Директория в которую надо
    :return:Выводит текущую директорию
    """
    if path_ == os.getcwd():
        return False
    try:
        os.chdir(path_)
        logging.info(f"cd {os.getcwd()}.")
    except Exception as e:
        logging.error({e})
        return False,print(f"{e}")
def cat(path_):
    """Выводит содержимого файла
    :param path_:путь к файлу
    :return ничего
    """
    if not path_:
        logging.error("Не указан файл")
        raise ValueError("Не указан файл")
    path_ = os.path.abspath(path_)
    if os.path.isdir(path_):
        logging.error(f"Является каталогом: {path_}")
        raise IsADirectoryError(f"Является каталогом: {path_}")
    try:
        file = open(path_)
        print(file.read())
        logging.info(f"cat {path_}.")
    except Exception as e:
        logging.error({e})
        return False,print(f"{e}")
def cp(arg,path_,path2_):
    """
    Копирование файлов
    :param arg: -r копирование рекурсивно
    :param path_: путь откуда копируешь
    :param path2_: путь куда копируешь
    :return: ничего
    """
    path_ = os.path.abspath(path_)
    path2_ = os.path.abspath(path2_)
    try:
        if arg == "-r":
            if os.path.isdir(path_):
                shutil.copytree(path_, path2_,dirs_exist_ok=True)
                logging.info(f"cp -r {path_,path2_}.")
            else:
                shutil.copy(path_, path2_)
                logging.info(f"cp {path_,path2_}.")
        else:
            shutil.copy(path_, path2_)
            logging.info(f"cp {path_, path2_}.")
    except Exception as e:
        logging.error({e})
        return False,print(f"{e}")
def mv(path_,path2_):
    """
    Перемещение файла
    :param path_: откуда переместить
    :param path2_: куда переместить
    :return: ничего
    """
    if path_ == "" or path2_ == "":
        logging.error("пустая директория")
        return False
    path_ = os.path.abspath(path_)
    path2_ = os.path.abspath(path2_)
    try:
        shutil.move(path_, path2_)
        logging.info(f"mv {path_, path2_}.")
    except Exception as e:
        logging.error({e})
        return False,print(f"{e}")
def rm(arg_,path_):
    """
    Удаление файлов
    :param arg_: -r удаление рекурсивно всего
    :param path_: путь того что удалить
    :return: ничего
    """
    path_ = os.path.abspath(path_)
    if path_ ==".." or path_ == "/":
        logging.error("Запрещено удалять такие каталоги")
        raise PermissionError("Запрещено удалять такие каталоги")
    try:
        if arg_ == "-r":
            directory_to_delete = Path(path_)
            shutil.rmtree(directory_to_delete)
            logging.info(f"rm -r{path_}.")
        else:
            file_to_delete = path_
            os.remove(file_to_delete)
            logging.info(f"rm {path_}.")
    except Exception as e:
        logging.error({e})
        return False,print(f"{e}")
def zip(archive,folder):
    """
    Зипует файл
    :param folder: файл для архивирования
    :param archive:  Имя будущего арзива
    :return: Ничего
    """
    try:
        shutil.make_archive(archive,'zip', folder)
        logging.info(f"zip {archive,folder}.")
    except Exception as e:
        logging.error({e})
        return False, print(f"{e}")
def unzip(archive):
    """
    Разархивирует
    :param archive: файл или каталог для разархивировки
    :return: Ничего
    """
    path_ = os.path.abspath(archive)
    try:
        shutil.unpack_archive(path_)
        logging.info(f"unzip {archive}.")
    except Exception as e:
        return False,print(f"{e}")
def tar(archive,folder):
    """
    Архивирует файл
    :param folder: файл для архивирования
    :param archive: Имя будущего арзива
    :return: Ничего
    """
    path_ = os.path.abspath(archive)
    try:
        shutil.make_archive(path_, 'gztar', folder)
        logging.info(f"tar {archive,folder}.")
    except Exception as e:
        logging.error({e})
        return False,print(f"{e}")
def untar(archive):
    """
    Разархивирует
    :param archive: файл или каталог для разархивировки
    :return:
    """
    path_ = os.path.abspath(archive)
    try:
        shutil.unpack_archive(path_)
        logging.info(f"untar {archive}.")
    except Exception as e:
        logging.error({e})
        return False,print(f"{e}")
def grep(arg,pattern,path_):
    """
    Поиск строк соответсвующих шаблону
    :param arg:флаг -i поиск без учета регистара и -r рекурскивный поиск в подкаталогах
    :param pattern:шаблон
    :param path_:Где искать
    :return:выводит имя файла номер строки и найденный фрагмент
    """
    path_ = os.path.abspath(path_)
    try:
        if arg == "-r":
            if os.path.isdir(path_):
                for root, files in os.walk(path_):
                    for file in files:
                        file_path = os.path.join(root, file)
                        with open(file_path, 'r') as f:
                            for line_num, line in enumerate(f, 1):
                                line = line.rstrip('\n\r')
                                if pattern.search(line):
                                    print(f"{file_path}:{line_num}: {line}")
                logging.info(f"grap {arg,path_,pattern}.")
            else:
                print("Чтобы использовать -r надо ввести каталог")
                logging.error("Чтобы использовать -r надо ввести каталог")
        else:
            with open(path_, 'r') as file:
                for line_num, line in enumerate(file, 1):
                    if pattern.search(line):
                        print(f"{path_}:{line_num}: {line.rstrip()}")
            logging.info(f"grap {arg, path_, pattern}.")
    except FileNotFoundError as e:
        logging.error({e})
        return False,print(f"{e}")
    except PermissionError as e:
        logging.error({e})
        return False, print(f"{e}")
    except IsADirectoryError as e:
        logging.error({e})
        return False, print(f"{e}")
    except UnicodeDecodeError as e:
        logging.error({e})
        return False, print(f"{e}")
    except Exception as e:
        logging.error({e})
        return False, print(f"{e}")
