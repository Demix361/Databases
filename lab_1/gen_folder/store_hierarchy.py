from random import randint


def get_store_amount(filename):
    i = 0

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            i += 1

    return i - 1


def generate_store_hierarchy(filename, store_db):
    store_amount = get_store_amount(store_db)

    with open(filename, 'w') as f:
        f.write('store_id,main_store\n')
        j = 0
        k = 5

        for i in range(store_amount):
            if i % k == 0:
                j += 1
                k = randint(2, 8)
            if i == 0:
                f.write(str(i + 1) + ',-\n')
            else:
                f.write(str(i + 1) + ',' + str(j) + '\n')


if __name__ == '__main__':
    generate_store_hierarchy('store_hierarchy.csv', 'store.csv')
