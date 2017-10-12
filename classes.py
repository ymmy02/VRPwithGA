class Individual(object):
  
  def __init__(self, chromosome):
    self.chromosome = chromosome
    self.distance = None
    self.fitness = None

  def __eq__(self, other):
    if other is None or type(self) != type(other): return False
    return self.chromosome == other.chromosome

  def __ne__(self, other):
    return not self.__eq__(other)

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


class NodeList(list):
  
  def __init__(self, capacity):
    list.__init__(self)
    self._capacity = capacity
    self._depot = None
    self._is_first_get_depot = True

  def get_depot(self):
    if self._is_first_get_depot:
      for node in self:
        if node.get_type() == 0:
          self._depot = node
          self._is_first_get_depot = False
          return self._depot
    return self._depot

  def get_customers(self):
    return [costomer for costomer in self if costomer.get_type()==1]

  def get_customers_id_list(self):
    return [costomer.get_id() for costomer in self if costomer.get_type()==1]

  def get_node_pos_from_id(self, id_):
    for node in self:
      if node.get_id() == id_:
        return node.get_pos()

  def is_feasible(self, route):
    amount = 0
    for node in self:
      if node.get_id() in route:
        amount += node.get_dem()
    is_feasible = (amount < self._capacity)
    return is_feasible
