"""Do not change these tests, they are meant to check your code and should fail"""
from app.calculations import Addition, Multiplication
from app.history import CalculationHistoryList as History


def test_history_operations():
    """Basic History Tests using the Instance"""
    my_tuple = (1, 2)
    addition_instance = Addition.create(my_tuple)
    assert isinstance(addition_instance, Addition), "Not an addition Instance"
    assert addition_instance.get_result() == 3, "Did not add 1 + 2 = 3"
    # Initializing a list

    addition_instance_1 = Addition.create(my_tuple)
    history = History(addition_instance, addition_instance_1)
    # Checking that the first element of the array is an addition instance
    assert isinstance(history[0], Addition)
    # Check how many items are in the list
    assert len(history) == 2, "Did not have 1 element in the list"
    # Removes all the elements in the list
    history.clear()
    assert len(history) == 0, "Did not clear"
    addition_instance_1 = Addition.create(my_tuple)
    addition_instance_2 = Addition.create(my_tuple)
    my_tuple = (1, 3)
    addition_instance_3 = Addition.create(my_tuple)
    # adding elements to existing list
    history.append(addition_instance_1)
    history.append(addition_instance_2)
    history.append(addition_instance_3)

    assert len(history) == 3, "There are not 3 elements in the list"
    # removing and loading an item in a list
    retrieve_instance = history.pop(-1)
    assert isinstance(retrieve_instance, Addition)
    assert len(history) == 2
    my_tuple = (2, 3)
    multiplication_instance1 = Multiplication.create(my_tuple)
    history.append(multiplication_instance1)
    history.print_history()
