import pytest

from ds.stack import Stack


@pytest.fixture
def stack():
    return Stack()


def test_constructor(stack):
    assert isinstance(stack, Stack)
    assert len(stack) == 0


def test_push(stack):
    stack.push(3)
    assert len(stack) == 1
    stack.push(5)
    assert len(stack) == 2


def test_pop(stack):
    stack.push("hello")
    stack.push("world")
    assert stack.pop() == "world"
    assert stack.pop() == "hello"
    assert stack.pop() == None
