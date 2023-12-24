# count how many words are in the file
def word_count(file_path: str):
    file = open(file_path, "rb")
    data = file.read()
    words = data.split()
    print(len(words))

# print how many times every word appear
def words_appear(file_path: str):
    file = open(file_path, "rb")
    data = file.read()
    words = data.split()
    word_hash_map = {}
    for word in words:
        if word in word_hash_map:
            word_hash_map[word] += 1
        else:
            word_hash_map[word] = 1

    for key in word_hash_map.keys():
        print(f"{key}: {word_hash_map.get(key)}")

def main():
    try:
        words_appear(r"C:\Users\Lenovo\PycharmProjects\omega_exercise\txt_files\file_1.txt")
        word_count(r"C:\Users\Lenovo\PycharmProjects\omega_exercise\txt_files\file_1.txt")
    except Exception as e:
        print(e)