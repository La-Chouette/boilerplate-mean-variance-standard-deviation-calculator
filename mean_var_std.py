import numpy as np

def calculate(list):
  m = np.array(list)
  print (m.reshape((3, 3)))
  meanX = np.sum(m, axis = 0)/3
  meanY = np.sum(m, axis = 1)/3
  meanF =np.sum(m)/9
  mean = [meanX,meanY,meanF]
  values = [mean, 0]
  parameters=['Mean','variance']
  calculations = dict(zip(parameters,values))
  
  return calculations