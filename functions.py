import math
import numpy as np

from classes import Node

###########
# Private #
###########
def _distance_between_nodes(node1_pos, node2_pos):
  diff = node1_pos - node2_pos
  return math.sqrt(diff.dot(diff))

def _calc_one_vehicle_distance(depot, nodes, route)
  total_distance = 0
  total_distance += _distance_between_nodes(depot, nodes[route[0]])

  for i in range(len(route)-1):
    node1_pos = nodes[route[i]].get_pos()
    node2_pos = nodes[route[i+1]].get_pos()
    total_distance += \
        _distance_between_nodes(node1_pos, node2_pos)

  total_distance += _distance_between_nodes(nodes[route[-1]], depot)

  return total_distance


##########
# Public #
##########
def calc_distance(nodes, routes):
  total_distance = 0
  for node in nodes:
    if node.get_type() == 0:    # Assume Only One Depot
      depot = node
      break

  for route in routes:
    total_distance += \
        _calc_one_vehicle_distance(depot, nodes, route)

  return total_distance


def weight_sum_evaluate(nvehicle, distance, w_nvehicle=100, w_distance=0.001):
  fitness = w_nvehicle*nvehicle + w_distance*distance
  return fitness
