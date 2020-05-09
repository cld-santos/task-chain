import sys
from random import choice, randint


def _read_words_from(file):
    words = []
    with open(file, "r") as word_file:
        for word in word_file:
            words.append(word[:-1])
    return words


def _address_from(words, number_of_addr_words=1):
    street_name = ""
    for number_of_words in range(number_of_addr_words):
        street_name += choice(words) + " "

    street_name = street_name.strip().lower()
    street_name = street_name[0].upper() + street_name[1:].lower().strip()

    return str(randint(1000, 9999)) + " " + street_name + ", #" + str(randint(100, 999))


def create_adresses_from(words_file, number_of_addresses=10):

    print("reading words from dictionary...")
    words = _read_words_from(words_file)
    print("words read.")

    print("creating addresses..")
    with open("addresses.txt", "a") as addresses:
        for n in range(number_of_addresses):
            addresses.write(_address_from(words, randint(2, 7)) + "\n")
    print("addresses created, have fun!")


if __name__ == '__main__':
    number_of_addresses = 10
    if len(sys.argv) > 2:
        words_file_name = sys.argv[1]
        number_of_addresses = int(sys.argv[2])
        create_adresses_from(words_file_name, number_of_addresses)
