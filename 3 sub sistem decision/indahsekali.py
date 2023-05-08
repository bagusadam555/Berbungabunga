import numpy as np
import math
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Load data
load = np.loadtxt('Trainingbaru.csv', delimiter=',')
TrainData = load[:, 0:4]
TrainClass = load[:, 4]

# Set the number of epochs
epoch = 10

# Set the input membership function type
in_mf_type = 'trap'

# Set the output membership function type
out_mf_type = 'constant'

# Set the range for splitting the data
split_range = 2

# Define the number of input variables
num_input = 4

# Train the ANFIS model
anfis_model = ANFIS.train(TrainData, TrainClass, split_range, num_input, in_mf_type, out_mf_type, dispOpt, epoch)

# Initialize Fuzzy Type-2 controller
fuzzy2_ctrl = ctrl.FuzzyControlSystem([], [])

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
    fuzzy2_ctrl.add_input(var)

output_var['low'] = fuzz.trimf(output_var.universe, [TrainClass.min(), TrainClass.min(), TrainClass.mean()])
output_var['medium'] = fuzz.trimf(output_var.universe, [TrainClass.min(), TrainClass.mean(), TrainClass.max()])
output_var['high'] = fuzz.trimf(output_var.universe, [TrainClass.mean(), TrainClass.max(), TrainClass.max()])
fuzzy2_ctrl.add_output(output_var)

# Define rules
rule1 = ctrl.Rule(input_vars[0]['low'] & input_vars[1]['low'] & input_vars[2]['low'] & input_vars[3]['low'], output_var['low'])
rule2 = ctrl.Rule(input_vars[0]['medium'] & input_vars[1]['medium'] & input_vars[2]['medium'] & input_vars[3]['medium'], output_var['medium'])
rule3 = ctrl.Rule(input_vars[0]['high'] & input_vars[1]['high'] & input_vars[2]['high'] & input_vars[3]['high'], output_var['high'])

# Add rules to the controller
fuzzy2_ctrl.add_rules(rule1, rule2, rule3)

# Evaluate the Fuzzy Type-2 controller
fuzzy2_pred = []
for i in range(len(TrainData)):
    inputs = [TrainData[i,j] for j in range(num_input)]
    fuzzy2_pred.append(fuzzy2_ctrl.compute(inputs))

# Save the Fuzzy Type-2 model
import numpy as np
np.savez('FuzzyType2_Model.npz', fuzzy2_ctrl=fuzzy2_ctrl, fuzzy2_pred=fuzzy2_pred)
