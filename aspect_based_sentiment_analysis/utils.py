import os
import pickle
import logging
from typing import Any
from typing import Iterable
from typing import List

logger = logging.getLogger('absa.utils')

def load(file_path: str):
    """ Load arbitrary python objects from the pickled file. """
    with open(file_path, mode='rb') as file:
        return pickle.load(file)


def save(data: Any, file_path: str):
    """ Save arbitrary python objects in the pickled file. """
    with open(file_path, mode='wb') as file:
        pickle.dump(data, file)


def batches(examples: Iterable[Any], batch_size: int,
            reminder: bool = True) -> Iterable[List[Any]]:
    """ Yield an example batch from the example iterable. """
    batch = []
    for example in examples:
        batch.append(example)
        if len(batch) < batch_size:
            continue
        yield batch
        batch = []
    # Return the last incomplete batch if it is necessary.
    if batch and reminder:
        yield batch

def cache_fixture(fixture):
    """ The function helps to cache test fixtures (only for test cases). """

    def wrapper(request, *args):
        name = request.fixturename
        val = request.config.cache.get(name, None)
        if not val:
            # Make sure that you pass the `request` argument.
            val = fixture(request, *args)
            request.config.cache.set(name, val)
        return val

    return wrapper
