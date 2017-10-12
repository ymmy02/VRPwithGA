import sys, os
import random

from classes import Individual
from data import loaddataset, visualize_result
from functions import calc_distance, make_pareto_ranking_list
import selection
import crossover
import mutation

POPULATION = 200
GSPAN = 100

def flatten(chromosome):
  return [node for route in chromosome for node in route]

def create_indviduals(population, nodes):
  indv_list = []
  customers_id_list = nodes.get_customers_id_list()

  for _ in range(population):
    chromosome = []
    size = len(customers_id_list)
    cut1 = 0
    cut2 = 0
    random.shuffle(customers_id_list)
    while cut1 < size:
      while True:
        cut2  = random.randint(cut1+1, size)
        route = customers_id_list[cut1:cut2]
        if nodes.is_feasible(route):
          break
      chromosome.append(route)
      cut1 = cut2
    indv = Individual(chromosome)
    indv_list.append(indv)

  return indv_list

def set_distance(nodes, indv_list):
  for indv in indv_list:
    indv.distance = calc_distance(nodes, indv.chromosome)

def remove_duplication(indv_list):
  nodupl_list = [indv_list[0]]
  for indv1 in indv_list[1:]:
    flag_add = True
    for indv2 in nodupl_list:
      if indv1 == indv2:
        flag_add = False
        break
    if flag_add:
      nodupl_list.append(indv1)
  return nodupl_list

def print_log(generation, indv_list):
  print("### Best Solutions of Generation " + str(generation) + " ###")
  pareto_ranking_list = make_pareto_ranking_list(indv_list)
  best_solutions = remove_duplication(pareto_ranking_list[0])
    
  for best_indv in best_solutions:
    vehicles = best_indv.get_nvehicle()
    distance = best_indv.distance
    print("Vehicles : " + str(vehicles) + " Distance : " + str(distance))

def does_end(loopcount):
  if loopcount > GSPAN:
    return True
  return False

def main(filename):

  ##############
  # Initialize #
  ##############
  print("#== LOADING DATASET FROM " + filename + " ==#")
  nodes = loaddataset(filename)
  parents = create_indviduals(POPULATION, nodes)
  offsprings = []
  set_distance(nodes, parents)
    
  #############
  # Main Loop #
  #############
  loopcount = 0
  while not does_end(loopcount):
    # Selection
    offsprings = selection.pareto_ranking(parents)
    # Crossover
    offsprings = crossover.best_cost_route_crossover(offsprings, nodes, rate=0.5)
    # Mutation
    offsprings = mutation.insertion(offsprings, nodes, rate=0.2, irate=0.02)
    # Change Generation
    parents = offsprings[:]
    # Calc Distance
    set_distance(nodes, parents)
    # Print Log
    loopcount += 1
    print_log(loopcount, parents)

  ##########################
  # Pick Up Best Solutions #
  ##########################
  pareto_ranking_list = make_pareto_ranking_list(parents)
  best_solutions = remove_duplication(pareto_ranking_list[0])

  #############
  # Visualize #
  #############
  visualize_result(nodes, best_solutions)

if __name__ == '__main__':
  argvs = sys.argv
  argc = len(argvs)
  # File Check
  if argc != 2:
    filename = 'dataset/A-n32-k05.xml'
  else:
    filename = argvs[1]
  if not os.path.exists(filename):
    print("!!!!! " + filename + " Does NOT Exist !!!!!")
    sys.exit()

  main(filename)
