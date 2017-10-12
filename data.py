import xml.etree.ElementTree as ET
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

from classes import Node, NodeList


def loaddataset(filename='dataset/A-n32-k05.xml'):
  tree = ET.parse(filename)
  root = tree.getroot()

  capacity = float(root.findall('.//capacity')[0].text)   # All vehicles have the same capacity
  nodes = NodeList(capacity)

  for node, request in zip(root.iter('node'), root.iter('request')):
    id_ = int(node.get('id'))
    type_ = int(node.get('type'))
    x = float(node.find('cx').text)
    y = float(node.find('cy').text)
    position = np.array([x, y])
    demand = float(request.find('quantity').text)
    node_ = Node(id_, type_, position, demand)
    nodes.append(node_)

  return nodes

def visualize_result(nodes, solutions):
  G = nx.Graph()
  depot = nodes.get_depot()
  # Add nodes
  G.add_node(depot.get_id(), pos=depot.get_pos(), color='blue')
  for customer in nodes.get_customers():
    G.add_node(customer.get_id(), pos=customer.get_pos(), color='red')

  for (index, solution) in enumerate(solutions):
    G.remove_edges_from(list(G.edges()))
    plt.clf()

    for route in solution.chromosome:
      G.add_edge(depot.get_id(), route[0])
      for i in range(len(route)-1):
        G.add_edge(route[i], route[i+1])
      G.add_edge(route[-1], depot.get_id())
      positions = nx.get_node_attributes(G,'pos')

    positions = {id_: (x, y) for (id_, (x, y)) in nx.get_node_attributes(G, 'pos').items()}
    #nx.draw(G, positions, with_labels=True, node_size=0)
    nx.draw(G, positions, with_labels=True)
    plt.savefig("solution" + str(index).zfill(3) + ".png")
