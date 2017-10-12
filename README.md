# Capacitated Vehicle Routing Problem Solver with GA

Language : Python3

## Assumption

- One single depot
- All vehicles have the same capacity

## Dataset

http://www.vrp-rep.org/datasets/item/2014-0000.html

## Python Libraries

### Input Data

- xml.etree.ElementTree

### Output Data

- matplotlib.pyplot
- networkx

### Others

- numpy
- random
- copy
- math

## Technique

- Pareto Ranking Selection
- Best Cost Route Crossover
- Insert Mutation

## Execution

```
$ python3 vrp.py [dataset_file]
```
ex
```
$ python3 vrp.py dataset/A-n32-k05.xml
```
