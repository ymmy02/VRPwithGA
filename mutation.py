import random
import copy

from functions import remove_null_route

###########
# Private #
###########
def _flatten(chromosome):
  return [node for route in chromosome for node in route]

def _random_choice_and_reinsert(chromosome, nodes):
  i = random.choice(range(len(chromosome)))
  j = random.choice(range(len(chromosome[i])))
  insert_node = chromosome[i].pop(j)
  feasible_list = []
  for (i, route) in enumerate(chromosome):
    if nodes.is_feasible(route+[insert_node]):
      feasible_list.append(i)
  if len(feasible_list) == 0:   # Is Empty
    chromosome.append([insert_node])
  else:
    i = random.choice(feasible_list)
    j = random.choice(range(len(chromosome[i])+1))
  chromosome[i].insert(j, insert_node)

def _insertion(chromosome, nodes, rate=0.02):
  size = len(_flatten(chromosome))
  for _ in range(size):
    if random.random() < rate:
      _random_choice_and_reinsert(chromosome, nodes)
      chromosome = remove_null_route(chromosome)
  return chromosome

##########
# Public #
##########
def insertion(offsprings, nodes, rate=0.2, irate=0.02):
  new_offsprings = []
  for indv in offsprings:
    tmp = copy.deepcopy(indv)
    if random.random() < rate:
      tmp.chromosome = _insertion(indv.chromosome, nodes, irate)
    tmp.chromosome = remove_null_route(tmp.chromosome)    # Remove the route which has no nodes
    new_offsprings.append(tmp)
  return new_offsprings
