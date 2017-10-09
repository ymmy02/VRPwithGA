#import numpy as np

class Individual(object):
  
  def __init__(self, chromosome):
    self.chromosome = chromosome
    self.distance = None
    self.fitness = None

  def get_nvehicle(self):
    nvehicle = len(self.chromosome)
    return nvehicle


class Node(object):

  def __init__(self, id_, type_, position, demand):
    self._id = id_
    self._type = type_
    self._position = position
    self._demand = demand

  # Getter
  def get_id(self):
    return self._id

  def get_type(self):
    return self._type

  def get_pos(self):
    return self._position

  def get_dem(self):
    return self._demand
