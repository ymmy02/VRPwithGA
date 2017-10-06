#import numpy as np

class Individual(object):
  
  def __init__(self, chromosome):
    self.chromosome = chromosome
    self.distance = None
    self.fitness = None

  def get_nvehicle():
    nvehicle = len(self.chromosome)
    return nvehicle


class Node(object):

  def __init__(self, id_, type_, position, demand):
    self.id_ = id_
    self.type_ = type_
    self.position = position
    self.demand = demand

  # Getter
  def get_id():
    return self.id_

  def get_type():
    return self.type_

  def get_pos():
    return self.position

  def get_dem():
    return self.demand
