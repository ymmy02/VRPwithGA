import random

###########
# Private #
###########
def _does_left_dominate_right(candidate, counterpart):
  numofvehicle1 = candidate.get_nvehicle()
  numofvehicle2 = counterpart.get_nvehicle()
  distance1 = candidate.distance
  distance2 = counterpart.distance

  if numofvehicle1 < numofvehicle2 and distance1 < distance2:
    return 1
  if numofvehicle1 > numofvehicle2 and distance1 > distance2:
    return -1
  return 0

def _make_pareto_ranking_list(current_rank_candidates):
  dominated_list = []
  nondominated_list = []

  for (i, candidate) in enumerate(current_rank_candidates):
    if candidate in dominated_list:
      break
    for counterpart in current_rank_candidates[i+1:]:
      does_left_dominate_right = \
          _does_left_dominate_right(candidate, counterpart)
      if does_left_dominate_right > 0:
        dominated_list.append(counterpart)
      else if does_left_dominate_right < 0:
        dominated_list.append(candidate)
        break
    nondominated_list.append(candidate)

  return nondominated_list, dominated_list


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


def pareto_ranking(parents):
  indv_list = parents
  ranking_list = []
  offsprings = []

  while len(indv_list) > 0:
    (current_rank_list, indv_list) = \
        _make_pareto_ranking_list(indv_list)
    ranking_list.append(current_rank_list)          

  size = len(ranking_list)
  npart = int((size*(size+1)) / 2)
  part = 1.0 / npart

  uniform = random.rand()

  span = 0.0
  for _ in range(len(parents)):
    for i in range(size):
      span += (size-i) * part
      if uniform < span:
        choice = random.choice(ranking_list[i])
        offsprings.append(choice)
        break
  
  return offsprings
