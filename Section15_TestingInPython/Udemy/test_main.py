from main import do_stuff


# positive test - succeeds
def test_do_stuff():
    test_param = 10
    result = do_stuff(test_param)
    assert result == 15


# negative test - succeeds
def test_do_stuff2():
    test_param = "alpha"
    result = do_stuff(test_param)
    assert isinstance(result, ValueError)


# empty test - succeeds
def test_do_stuff3():
    test_param = None
    result = do_stuff(test_param)
    assert result == 'please enter number'


# empty test - succeeds
def test_do_stuff4():
    test_param = ''
    result = do_stuff(test_param)
    assert result == "please enter number"
