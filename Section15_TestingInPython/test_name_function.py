from name_function import get_formatted_name


def test_first_last_name():
    # Do names like ' Janis Joplin' work?
    formatted_name = get_formatted_name('janis', 'joplin')
    assert formatted_name == 'Janis Joplin'
    # assert condition (boolean expression you expect to always be true), [optional_error_message]
    # The assert keyword is used in Python for debugging and defensive programming. It allows you to insert sanity checks into your code to catch potential errors and unexpected conditions during development.

def test_first_last_middle_name():
    # Do names like ' Wolfgang Amadeus Mozart' work?
    formatted_name = get_formatted_name(
        'wolfgang', 'mozart', 'amadeus')
    assert formatted_name == 'Wolfgang Amadeus Mozart'