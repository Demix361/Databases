from random import randint, choice, random, shuffle
from faker import Faker


class Client():
    def __init__(self):
        self.first_name = None
        self.last_name = None
        self.sex = None
        self.phone = None
        self.email = None
        self.status = None


def get_name_pool(amount):
    fake = Faker("ru-RU")
    female = []
    male = []

    for i in range(amount):
        fio = fake.name().split()
        if len(fio) != 3:
            fio = fio[1:]

        if fio[2][-1] == "а":
            female.append(fio[:2])
        elif fio[2][-1] == "ч":
            male.append(fio[:2])

    return male, female


def get_phone_pool(amount):
    pool = []
    nums = 9999999999

    for i in range(amount):
        phone = '+7' + '0' * (10 - len(str(nums))) + str(nums)
        pool.append(phone)
        nums -= 1

    shuffle(pool)
    return pool


def translit(word):
    abc = [('а', 'a'), ('б', 'b'), ('в', 'v'), ('г', 'g'), ('д', 'd'), ('е', 'e'), ('ё', 'yo'), ('ж', 'zh'), ('з', 'z'),
           ('и', 'i'), ('й', 'y'), ('к', 'k'), ('л', 'l'), ('м', 'm'), ('н', 'n'), ('о', 'o'), ('п', 'p'), ('р', 'r'),
           ('с', 's'), ('т', 't'), ('у', 'u'), ('ф', 'f'), ('х', 'h'), ('ц', 'c'), ('ч', 'ch'), ('ш', 'sh'), ('щ', 'sh'),
           ('ь', ''), ('ы', 'i'), ('ъ', ''), ('э', 'e'), ('ю', 'yu'), ('я', 'ya')]

    new = ''
    word = word.lower()

    for sym in word:
        for c in abc:
            if c[0] == sym:
                new += c[1]

    return new


def gen_email(f_name, l_name):
    f_name = translit(f_name)
    l_name = translit(l_name)
    email = ''

    a = randint(0, 1)
    n = randint(0, 3)
    if a == 0:
        beg = f_name[:len(f_name) - randint(0, len(f_name) - 1)]
    else:
        beg = l_name[:len(l_name) - randint(0, len(l_name) - 1)]
    email += beg

    if n == 1:
        email += str(randint(10, 999))

    sep = ['.', '-', '_']
    email += choice(sep)

    if n == 2:
        email += str(randint(10, 999))

    if a == 0:
        end = l_name
    else:
        end = f_name
    email += end

    if n == 3:
        email += str(randint(10, 999))

    email += '@'

    adr = ['yandex.ru', 'ya.ru', 'yandex.com', 'gmail.com', 'mail.ru', 'yahoo.com', 'rambler.ru']
    email += choice(adr)

    return email


def get_status():
    sts = [("bronze", 45), ("silver", 30), ("gold", 18), ("diamond", 12)]

    num = random() * 100
    s = 0

    for i in range(len(sts)):
        s += sts[i][1]

        if num < s:
            return sts[i][0]

    return None


def to_line(*args):
    n = len(args)
    res = ""

    for i in range(n):
        res += str(args[i])

        if i == n - 1:
            res += "\n"
        else:
            res += ","

    return res


def generate_client(amount, filename):
    clients = []
    male, female = get_name_pool(2000)
    phone_pool = get_phone_pool(amount)
    table_header = "first_name,last_name,sex,phone,email,status\n"

    for i in range(amount):
        client = Client()
        if randint(0, 1) == 0:
            client.last_name, client.first_name = choice(male)
            client.sex = "male"
        else:
            client.last_name, client.first_name = choice(female)
            client.sex = "female"
        client.phone = phone_pool[i]
        client.email = gen_email(client.first_name, client.last_name)
        client.status = get_status()

        clients.append(client)

    with open(filename, "w", encoding="utf-8") as f:
        f.write(table_header)
        for c in clients:
            f.write(to_line(c.first_name, c.last_name, c.sex, c.phone, c.email, c.status))


if __name__ == "__main__":
    generate_client(1000, "client.csv")
