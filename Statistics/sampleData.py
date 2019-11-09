from random import random


def sampleData(data, sample_size):
    random_sample = random.sample(data, k=sample_size)
    return random_sample