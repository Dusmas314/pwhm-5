from Decorator_2 import logger

class FlatIterator:

    @logger('test.txt')
    def __init__(self, list_of_list):
        self.list = []
        for current_list in list_of_list:
            for element in current_list:
                self.list.append(element)

    @logger('test.txt')
    def __iter__(self):
        self.counter = -1
        return self

    def __next__(self):
        self.counter += 1
        if self.counter == len(self.list):
            raise StopIteration
        return self.list[self.counter]


@logger('test.txt')
def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
