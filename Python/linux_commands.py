import os

while (True):
    print("1 - PWD")
    print("2 - List directories")
    print("3 - Create a file")
    print("4 - Create a dir")
    print("5 - Remove a dir/file")
    print("6 - List processes")
    print("7 - Rename file")

    option = input("Enter the chosen number for the respective action:")

    match option:
        case "1":
            os.system('pwd')

        case "2":
            os.system('ls -l')

        case "3":
            file_name = input("Enter file name:")
            os.system('touch' + file_name)

        case "4":
            dir_name = input("Enter directory name:")
            os.system('mkdir' + dir_name)

        case "5":
            rmdir_name = input("Enter the directory's name you want to remove")
            os.system('rm' + rmdir_name)

        case "6":
            os.system('ps')

        case "7":
            og_file_name = input("Enter name file")
            new_file_name = input("Enter new name")
            os.system('mv' + og_file_name + new_file_name)

