def main():
    file_1 = open(r"C:\Users\Lenovo\PycharmProjects\omega_exercise\txt_files\file_1.txt", "rb")
    file_2 = open(r"C:\Users\Lenovo\PycharmProjects\omega_exercise\txt_files\file_2.txt", "rb")
    file_3 = open(r"C:\Users\Lenovo\PycharmProjects\omega_exercise\txt_files\file_3.txt", "wb")

    file_3.write(file_1.read())
    file_3.write(file_2.read())

    file_1.close()
    file_2.close()
    file_3.close()








