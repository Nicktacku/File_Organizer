import os
import shutil


def by_keyword():
    path = input("Enter path directory: ")
    keyword = input("Enter keyword: ")
    files = os.listdir(path)

    for file in files:
        file_name, _ = os.path.splitext(file)

        keyword_path = path + "/" + keyword
        file_path = path + "/" + file

        if keyword.lower() in file_name.lower():
            if os.path.exists(keyword_path):
                shutil.move(file_path, keyword_path + "/" + file)
            else:
                os.makedirs(keyword_path)
                shutil.move(file_path, keyword_path + "/" + file)


def by_type():
    path = input("Enter path directory: ")
    files = os.listdir(path)

    for file in files:
        filename, type = os.path.splitext(file)
        type = type[1:]

        type_path = path + "/" + type
        file_path = path + "/" + file

        if os.path.exists(type_path):
            shutil.move(file_path, type_path + "/" + file)
        else:
            os.makedirs(type_path)
            shutil.move(file_path, type_path + "/" + file)


done = False

while not done:
    os.system("cls")
    print("File Organizer:")
    print()
    print("Choose how you want to organize the files")
    print("a. By Keyword")
    print("b. By type")
    print("c. Exit")
    print()
    choice = input("Enter Choice: ").lower()

    if choice == "a":
        by_keyword()
        print("done")
    elif choice == "b":
        by_type()
        print("done")
    elif choice == "c":
        done = True

print()
print("Thank you for using the program")
