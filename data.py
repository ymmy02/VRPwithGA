import xml.etree.ElementTree as ET
import numpy as np

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
