import pytest
import random
from asyncio_queue_rotation import RotationQueue


@pytest.mark.asyncio
async def test_rotation_queue_is_empty():
    rotation_queue = RotationQueue(1)
    await rotation_queue.put(1)
    await rotation_queue.get()
    assert rotation_queue.empty(), 'Queue not empty'


@pytest.mark.asyncio
async def test_rotation_queue_put():
    rotation_queue = RotationQueue(1)
    vars = tuple(
        random.random() for _ in range(4)
    )
    print(vars)
    for v in vars:
        await rotation_queue.put(v)
    assert rotation_queue.qsize() == 1, 'Rotation queue qsize not equal 1'


@pytest.mark.asyncio
async def test_rotation_queue_get():
    rotation_queue = RotationQueue(1)
    vars = tuple(
        random.random() for _ in range(4)
    )
    print(vars)
    for v in vars:
        await rotation_queue.put(v)
    value = await rotation_queue.get()
    assert rotation_queue.empty(), 'Queue is empty'
    assert value == vars[-1], 'And Value last'
