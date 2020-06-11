#!/usr/bin/env python3

import pandas as pd

# TODO: Set weight1, weight2, and bias for the logical 'AND' function
weight1 = 0
weight2 = -1
bias = 0


# DON'T CHANGE ANYTHING BELOW
# Inputs and outputs
test_inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]
correct_outputs = [True, False, True, False]
outputs = []

# Generate and check output
for test_input, correct_output in zip(test_inputs, correct_outputs):
    linear_comb = weight1 * test_input[0] + weight2 * test_input[1] + bias
    output = int(linear_comb >= 0)
    is_correct_str = 'Yes' if output == correct_output else 'No'
    outputs.append([test_input[0],
                    test_input[1],
                    linear_comb,
                    output, is_correct_str])

# Print output
num_wrong = len([output[4] for output in outputs if output[4] == 'No'])
c1 = 'Input 1'
c2 = '  Input 2'
c3 = '  Linear Combination'
c4 = '  Activation Output'
c5 = '  Is Correct'

output_frame = pd.DataFrame(outputs, columns=[c1, c2, c3, c4, c5])
if not num_wrong:
    print('Nice!  You got it all correct.\n')
else:
    print('You got {} wrong.  Keep trying!\n'.format(num_wrong))
print(output_frame.to_string(index=False))
