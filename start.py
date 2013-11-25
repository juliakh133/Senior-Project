# Description: 
# Generates the initial matrices, A and B. The elements of A and B are from
# the cross product Z(n) x Z(n), n integer.
# We first generate the Z(n) set and then, using the indices of the elements
# of that set, we randomly assign them to position in A and B.

# Runs the algorithms set in the config.yaml file

# Author:   Vlad Burca
# Date:     November 13, 2013
# Updated:  November 24, 2013

import yaml
import numpy 
from numpy import linalg

import helpers
import algorithms

# Constant names for the Explicit Methods
ANGLUIN_METHOD  = 'ANGLUIN'
MARGULIS_METHOD = 'MARGULIS'

# Constant names for the Random Methods
RANDOM_3        = 'RANDOM_3'
RANDOM_5        = 'RANDOM_5'


# MAIN

def generate_expanders():
  # Read n from configuration file
  config_file = open("config.yaml", "r")
  config_vars = yaml.safe_load(config_file)
  config_file.close()


  # Clean existing .out files
  if config_vars['params']['cleanup'] == True:
    helpers.cleanup(".out")

  # Clean existing .results files
  if config_vars['params']['clear_results_files'] == True:
    helpers.cleanup(".results")


  n       = config_vars['params']['n']
  EPSILON = config_vars['params']['epsilon']

  print "Generating matrices A and B with n = " + str(n) + " ... "

  # Generate Z(n)
  #Z_n = list(xrange(n))


  # Generate the elements of  A and B using indices from the cross product
  size = n * n

  indices_of_pairs = numpy.arange(size)   # Generate array of indices of the cross product

  A_indices = numpy.random.permutation(indices_of_pairs).reshape((n, n)) # Randomize in matrix positions
  B_indices = numpy.random.permutation(indices_of_pairs).reshape((n, n)) # Randomize in matrix positions

  if config_vars['params']['output_indices_matrices'] == True:
    helpers.write_indices_matrices(A_indices, B_indices)

  if config_vars['params']['output_initializer_matrices'] == True:
    returned_matrices = helpers.generate_pair_matrices(A_indices, B_indices, n)
    A = returned_matrices[0]
    B = returned_matrices[1]

    helpers.write_pair_matrices(A, B)

  print "Generated matrices A and B."


  if config_vars['algorithms']['angluin_method'] == True:
    print ''
    algorithms.EXPLICIT_METHOD(ANGLUIN_METHOD, size, A_indices, n, EPSILON)

  if config_vars['algorithms']['margulis_method'] == True:
    print ''
    algorithms.EXPLICIT_METHOD(MARGULIS_METHOD, size, A_indices, n, EPSILON)

  if config_vars['algorithms']['random_3'] == True:
    print ''
    algorithms.RANDOM_METHOD(RANDOM_3, 2 * size, EPSILON)

  if config_vars['algorithms']['random_5'] == True:
    print ''
    algorithms.RANDOM_METHOD(RANDOM_5, 2 * size, EPSILON)

print '\n'
# DEBUGGING CODE

generate_expanders()
