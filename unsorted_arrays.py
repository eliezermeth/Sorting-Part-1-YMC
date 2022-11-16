import person

class UnsortedArrays:

    def get_number_array_1(self):
        return [4, 7, 235, 0, 1]

    def get_number_array_2(self):
        return [83, 12, 0, 32, 876, 32, 1, 0, -1, 4]

    def get_string_array(self):
        return ["oranges", "bananas", "cantaloupes", "zucchini", "apples", "quinoa"]

    def get_people_array(self):
        # create clean person array
        self.people = []
        # list person data
        names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"]
        ids = [9, 4, 19, 2, 1, 10]
        ages = [34, 18, 67, 39, 3, 19]

        # create person array
        for i in range(len(names)):
            self.people.append(person.Person(names[i], ids[i], ages[i]))

        return self.people
