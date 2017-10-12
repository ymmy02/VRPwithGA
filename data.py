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
  colors = ['black', 'green', 'cyan', 'magenta', 'red', 'blue']

  # Add nodes
  G.add_node(depot.get_id(), pos=depot.get_pos(), color='blue')
  for customer in nodes.get_customers():
    G.add_node(customer.get_id(), pos=customer.get_pos(), color='red')

  for (index, solution) in enumerate(solutions):
    edge_list = []
    G.remove_edges_from(list(G.edges()))
    plt.clf()

    for route in solution.chromosome:
      edges = []
      edges.append((depot.get_id(), route[0]))
      for i in range(len(route)-1):
        edges.append((route[i], route[i+1]))
      edges.append((route[-1], depot.get_id()))
      edge_list.append(edges)

    for edges in edge_list:
      G.add_edges_from(edges)

    # Draw Nodes
    positions = {id_: (x, y) for (id_, (x, y)) in nx.get_node_attributes(G, 'pos').items()}
    nx.draw(G, positions, with_labels=True)
    nx.draw_networkx_nodes(G,positions,
                           nodelist=[depot.get_id()],
                           node_color='blue',)
    nx.draw_networkx_nodes(G,positions,
                           nodelist=nodes.get_customers_id_list(),
                           node_color='r',)
    # Draw Edges
    for (i, edges) in enumerate(edge_list):
      nx.draw_networkx_edges(G,positions,
                             edgelist=edges,
                             edge_color=colors[i%(len(colors))])

    plt.savefig("solution" + str(index).zfill(3) + ".png")
