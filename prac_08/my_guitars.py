"""Main client code for testing Guitar class"""

from prac_08.guitars import Guitar
FILE_NAME = "guitars.csv"


def main():
    print("My guitars!")
    continue_loop = False

    list_of_guitars = load_file()
    list_of_guitars = create_guitars(list_of_guitars)
    # Input loop set to False for testing
    # User addition to guitars
    # while continue_loop:
    #     guitar_name = input("Please enter a Name: ")
    #     if guitar_name.strip() == "":
    #         continue_loop = False
    #     else:
    #         guitar_year = int(input("Please enter the Year: "))
    #         guitar_cost = float(input("Please enter the Cost: "))
    #
    #         guitars.append(Guitar(guitar_name, guitar_year, guitar_cost))

    # Print list
    if list_of_guitars:
        print("These are my guitars:")

        for i, guitar in enumerate(list_of_guitars, 1):
            vintage = "(vintage)" if guitar.is_vintage() else ""

            print("Guitar {}: {:>20} ({}), worth ${:10,.2f} {}".format(
                i, guitar.name, guitar.year, guitar.cost, vintage))


def load_file():
    """Open file and clean data; return list of tuples"""
    list_of_data = []
    data_file = open(FILE_NAME, "r")
    for line in data_file:
        line = line.strip().split(",")
        list_of_data.append(tuple(line))
    data_file.close()

    return list_of_data


def create_guitars(guitars):
    class_list = []
    for i, guitar in enumerate(guitars):
        class_list.append(Guitar(guitar[0], int(guitar[1]), float(guitar[2])))
    return class_list


main()
