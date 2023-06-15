import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Load data
load = np.loadtxt('sub3/trainingcopy.csv', delimiter=',')
TrainData = load[:, 0:4]
TrainClass = load[:, 4]

# Set the number of epochs
epoch = 10

# Set the input membership function type
in_mf_type = 'trap'

# Set the output membership function type
out_mf_type = 'constant'

# Define the number of input variables
num_input = 4

# Define input variables
input_vars = []
for i in range(num_input):
    var_name = 'x' + str(i+1)
    var = ctrl.Antecedent(np.arange(TrainData[:,i].min(), TrainData[:,i].max(), 1), var_name)
    input_vars.append(var)

# Define output variable
output_var = ctrl.Consequent(np.arange(TrainClass.min(), TrainClass.max(), 1), 'y')

# Create Fuzzy Type-2 membership functions
for i in range(num_input):
    var = input_vars[i]
    var['low'] = fuzz.trapmf(var.universe, [TrainData[:,i].min(), TrainData[:,i].min(), TrainData[:,i].mean(), TrainData[:,i].mean()])
    var['medium'] = fuzz.trapmf(var.universe, [TrainData[:,i].min(), TrainData[:,i].mean(), TrainData[:,i].mean(), TrainData[:,i].max()])
    var['high'] = fuzz.trapmf(var.universe, [TrainData[:,i].mean(), TrainData[:,i].mean(), TrainData[:,i].max(), TrainData[:,i].max()])

# Define rules
rule1 = ctrl.Rule(input_vars[0]['low'] & input_vars[1]['low'] & input_vars[2]['low'] & input_vars[3]['low'], output_var['low'])
rule2 = ctrl.Rule(input_vars[0]['medium'] & input_vars[1]['medium'] & input_vars[2]['medium'] & input_vars[3]['medium'], output_var['medium'])
rule3 = ctrl.Rule(input_vars[0]['high'] & input_vars[1]['high'] & input_vars[2]['high'] & input_vars[3]['high'], output_var['high'])

# Create Fuzzy Type-2 controller
fuzzy2_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])

# Create simulation
simulation = ctrl.ControlSystemSimulation(fuzzy2_ctrl)

# Evaluate the Fuzzy Type-2 controller
fuzzy2_pred = []
for i in range(len(TrainData)):
    for j in range(num_input):
        simulation.input[input_vars[j].name] = TrainData[i][j]
    simulation.compute()
    fuzzy2_pred.append(simulation.output[output_var.name])

# Save the Fuzzy Type-2 model
np.savez('FuzzyType2_Model.npz', fuzzy2_ctrl=fuzzy2_ctrl, fuzzy2_pred=fuzzy2_pred)
