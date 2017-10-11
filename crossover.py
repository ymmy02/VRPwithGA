import random
import copy
import time

from functions import remove_null_route

###########
# Private #
###########
def _insert_node(nodes, new_chromosome, L):
  for insert_node in L:
    feasible_list = []
    for (i, route) in enumerate(new_chromosome):
      if nodes.is_feasible(route+[insert_node]):
        feasible_list.append(i)
    if len(feasible_list) == 0:   # Is Empty
      new_chromosome.append([insert_node])
    else:
      i = random.choice(feasible_list)
      j = random.choice(range(len(new_chromosome[i])+1))
      new_chromosome[i].insert(j, insert_node)

#===<Route Crossover>===#
def _flatten(chromosome):
  return [node for route in chromosome for node in route]

def _mask(chromosome):
  L = []
  new_chromosome = []
  for route in chromosome:
    if random.random() < 0.5:
      L.extend(route)
    else:
      new_chromosome.append(route)
  return L, new_chromosome

def _rearrange_in_counterpart_order(L, ch_onerow):
  return [i for i in ch_onerow if i in L]
  
def _route_crossover(nodes, ch1, ch2):
  L1, new_ch1 = _mask(ch1)
  L2, new_ch2 = _mask(ch2)
  ch1_onerow = _flatten(ch1)
  ch2_onerow = _flatten(ch2)
  L1 = _rearrange_in_counterpart_order(L1, ch2_onerow)
  L2 = _rearrange_in_counterpart_order(L2, ch1_onerow)
  _insert_node(nodes, new_ch1, L1)
  _insert_node(nodes, new_ch2, L2)

  return new_ch1, new_ch2
#===</Route Crossover>===#

#===<Best Cost Route Crossover>===#
def _delete_nodes(chromosome, route):
  remove_index_list = []
  chromosome_deleated = []
  for rt in chromosome:
    route_deleated = [node for node in rt if node not in route]
    chromosome_deleated.append(route_deleated)
  return chromosome_deleated

def _best_cost_route_crossover(nodes, ch1, ch2):
  route1 = random.choice(ch1)
  route2 = random.choice(ch2)
  ch1 = _delete_nodes(ch1, route2)
  ch2 = _delete_nodes(ch2, route1)
  _insert_node(nodes, ch1, route2)
  _insert_node(nodes, ch2, route1)
  return ch1, ch2
#===</Best Cost Route Crossover>===#

##########
# Public #
##########
def route_crossover(offsprings, nodes, rate=0.5):
  new_offsprings = []
  half = len(offsprings)/2

  for (indv1, indv2) in zip (offsprings[0:half], offsprings[half:]):
    tmp1 = copy.deepcopy(indv1)
    tmp2 = copy.deepcopy(indv2)
    if random.random() < rate:
      (tmp1.chromosome, tmp2.chromosome) =        \
          _route_crossover(nodes, indv1.chromosome, indv2.chromosome)
    tmp1.chromosome = remove_null_route(tmp1.chromosome)   # Remove the route which has no nodes
    tmp2.chromosome = remove_null_route(tmp2.chromosome)
    new_offsprings.append(tmp1)
    new_offsprings.append(tmp2)
  return new_offsprings


def best_cost_route_crossover(offsprings, nodes, rate=0.5):
  new_offsprings = []
  half = int(len(offsprings)/2)

  for (indv1, indv2) in zip (offsprings[0:half], offsprings[half:]):
    tmp1 = copy.deepcopy(indv1)
    tmp2 = copy.deepcopy(indv2)
    if random.random() < rate:
      (tmp1.chromosome, tmp2.chromosome) =        \
          _best_cost_route_crossover(nodes, indv1.chromosome, indv2.chromosome)
    tmp1.chromosome = remove_null_route(tmp1.chromosome)   # Remove the route which has no nodes
    tmp2.chromosome = remove_null_route(tmp2.chromosome)
    new_offsprings.append(tmp1)
    new_offsprings.append(tmp2)
  return new_offsprings
