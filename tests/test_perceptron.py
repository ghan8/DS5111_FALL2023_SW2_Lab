import os
import sys
import pytest
import platform
sys.path.append(".")

from bin.perceptron import Perceptron

def test_perceptron():
    the_perceptron = Perceptron()
    the_perceptron.train([
        [1, 1],
        [1, 0],
        [0, 1],
        [0, 0],
    ], [1, 1, 1, 0])

    assert the_perceptron.predict([1, 1]) == 1, "Test failed [1, 1]"
    assert the_perceptron.predict([1, 0]) == 1, "Test failed [1, 0]"
    assert the_perceptron.predict([0, 1]) == 1, "Test failed [0, 1]"
    assert the_perceptron.predict([0, 0]) == 0, "Test failed [0, 0]"

@pytest.mark.xfail
def test_perceptron_negative():
    the_perceptron = Perceptron()
    the_perceptron.train([
        [1, 1],
        [1, 0],
        [0, 1],
        [0, 0],
    ], [1, 1, 1, 0])

    assert the_perceptron.predict([0, 0]) == 1, "Negative test should fail"

@pytest.mark.skipif(
    'Linux' not in platform.platform() and 'aws' not in platform.platform(),
    reason="Test is skipped on Linux AWS instances.")
def test_linux_only():

    # Getting all memory using os.popen()
    total_memory, used_memory, free_memory = map(int, os.popen('free -t -m').readlines()[-1].split()[1:])

    print(total_memory)
    print(used_memory)
    print(free_memory)  
    assert True

test_linux_only()

@pytest.mark.skip(reason="This test is not yet ready for prime time")
def test_always_skipped():
    # this silly python functionality is still in dev
    print("waiting on other people to do there job")
    assert True, "Test should always skip because this functionality is still in development"

@pytest.mark.parametrize("trainingset, labels, expected", [
    ([[1, 1], [1, 0], [0, 1], [0, 0]], 
        [1, 0, 0, 0], [1, 0, 0, 0]),
    ([[1, 1], [1, 0], [0, 1], [0, 0]],
        [0, 0, 0, 1], [0, 0, 0, 1]),
    ([[1, 1], [1, 0], [0, 1], [0, 0]], 
        [1, 1, 0, 0], [1, 1, 0, 0]),
    ([[1, 1], [1, 0], [0, 1], [0, 0]],
        [1, 1, 1, 1], [1, 1, 1, 1]),
    ([[1, 1], [1, 0], [0, 1], [0, 0]], 
        [1, 1, 1, 0], [1, 1, 1, 0])
])
def test_perceptron_multi(trainingset, labels, expected):
    test_perceptron = Perceptron()
    test_perceptron.train(trainingset, labels)

    for i, input_data in enumerate(trainingset):
        prediction = test_perceptron.predict(input_data)
        assert prediction == expected[i], f"Failed: {input_data} should predict {expected[i]}"
