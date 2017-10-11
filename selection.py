import random

from functions import make_pareto_ranking_list

###########
# Private #
###########

##########
# Public #
##########
#===!!! Must Have Fitness !!!===#
def tournament(parents, tournament_size=3):
  offsprings = []
  for _ in range(len(parents)):
    minfitness = 1e14
    samples = random.sample(parents, tournament_size)
    for salesman in samples:
      if salesman.fitness < minfitness:
        tmp = salesman
        minfitness = salesman.fitness
    offsprings.append(tmp)
  return offsprings 


def _flatten(chromosome):
  return [node for route in chromosome for node in route]

def pareto_ranking(parents):
  indv_list = parents
  ranking_list = []
  offsprings = []

  ranking_list = make_pareto_ranking_list(indv_list)

  size = len(ranking_list)
  npart = int((size*(size+1)) / 2)
  part = 1.0 / npart

  uniform = random.random()

  span = 0.0
  for _ in range(len(parents)):
    for i in range(size):
      span += (size-i) * part
      if uniform < span:
        choice = random.choice(ranking_list[i])
        offsprings.append(choice)
        break
  
  return offsprings
