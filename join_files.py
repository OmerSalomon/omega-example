def joinFiles(str_file_1, str_file_2, str_file_3):
    file_1 = open(str_file_1, "rb")
    file_2 = open(str_file_2, "rb")
    file_3 = open(str_file_3, "wb")

    file_3.write(file_1.read())
    file_3.write(file_2.read())

    file_1.close()
    file_2.close()
    file_3.close()


def main():
    str_file_1 = input()
    str_file_2 = input()
    str_file_3 = input()
    try:
        joinFiles(str_file_1, str_file_2, str_file_3)
    except Exception as e:
        print(e)










