# basic person class
class Person:
    def __init__(self, first_name: str, last_name: str, age: int):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

# talker class inherit from person
class Talker(Person):
    def talk(self, txt):
        pass


# happy talker class inherit from talker
class HappyTalker(Talker):
    def talk(self, txt: str):
        print(f"{txt}!!!")

# slow talker class inherit from talker
class SlowTalker(Talker):
    def talk(self, txt: str):
        print(' '.join(txt))

# stutter talker class inherit from talker
class StutterTalker(Talker):
    def talk(self, txt: str):
        words = txt.split()
        stuttered_words = [''.join([word[0] * 2, word]) for word in words]
        result = ' '.join(stuttered_words)
        print(result)


def makeThemTalk(persons_list: list[Person], txt: str):
    for person in persons_list:
        if person.age > 10 and type(person) == Talker:
            person.talk(txt)


def main():
    person1 = StutterTalker("omer", "salomon", 12)
    person2 = SlowTalker("omer", "salomon", 12)
    person3 = HappyTalker("omer", "salomon", 12)
    try:
        person_list = [person1, person2, person3]
        makeThemTalk(person_list, "I love cookie")
    except Exception as e:
        print(e)
