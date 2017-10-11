import math

from classes import Node

###########
# Private #
###########
def _distance_between_nodes(node1_pos, node2_pos):
  diff = node1_pos - node2_pos
  return math.sqrt(diff.dot(diff))

def _calc_one_vehicle_distance(nodes, route):
  depot_pos = nodes.get_depot().get_pos()   # Assume Only one depot
  total_distance = 0
  first_node_pos = nodes.get_node_pos_from_id(route[0])
  total_distance += \
      _distance_between_nodes(depot_pos, first_node_pos)
  for i in range(len(route)-1):
    node1_pos = nodes.get_node_pos_from_id(route[i])
    node2_pos = nodes.get_node_pos_from_id(route[i+1])
    total_distance += \
        _distance_between_nodes(node1_pos, node2_pos)
  last_node_pos = nodes.get_node_pos_from_id(route[-1])
  total_distance += \
      _distance_between_nodes(last_node_pos, depot_pos)
  return total_distance

def _does_left_dominate_right(candidate, counterpart):
  numofvehicle1 = candidate.get_nvehicle()
  numofvehicle2 = counterpart.get_nvehicle()
  distance1 = candidate.distance
  distance2 = counterpart.distance

  if numofvehicle1 == numofvehicle2 and distance1 == distance2:
    return 0
  if numofvehicle1 <= numofvehicle2 and distance1 <= distance2:
    return 1
  if numofvehicle1 >= numofvehicle2 and distance1 >= distance2:
    return -1
  return 0

def _make_current_ranking_list(current_rank_candidates): 
  dominated_list = []
  nondominated_list = []

  for (i, candidate) in enumerate(current_rank_candidates):
    flag_dominated = False
    if candidate in dominated_list:
      continue
    for counterpart in current_rank_candidates[i+1:]:
      if counterpart in dominated_list:
        continue
      does_left_dominate_right = \
          _does_left_dominate_right(candidate, counterpart)
      if does_left_dominate_right > 0:
        dominated_list.append(counterpart)
      elif does_left_dominate_right < 0:
        flag_dominated = True
        dominated_list.append(candidate)
        break
    if not flag_dominated:
      nondominated_list.append(candidate)

  return nondominated_list, dominated_list

##########
# Public #
##########
def calc_distance(nodes, chromosome):
  total_distance = 0
  for route in chromosome:
    total_distance += \
        _calc_one_vehicle_distance(nodes, route)
  return total_distance


def weight_sum_evaluate(nvehicle, distance, w_nvehicle=100, w_distance=0.001):
  fitness = w_nvehicle*nvehicle + w_distance*distance
  return fitness


def remove_null_route(chromosome):
  return [route for route in chromosome if len(route) != 0]


def make_pareto_ranking_list(indv_list):
  ranking_list = []
  while len(indv_list) > 0:
    (current_rank_list, indv_list) = \
        _make_current_ranking_list(indv_list)
    ranking_list.append(current_rank_list)          
  return ranking_list
