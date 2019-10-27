# Neural Network.
# Without Numpy - only clean Python.
import random
from math import exp


class NeuralNetwork:
    def __init__(self, layers=3, layer_nodes=3, learning_rate=0.1):
        self.layers = layers
        self.layer_nodes = layer_nodes
        self.learning_rate = learning_rate

        # generate weights
        self.weights = [
            [
                [random.uniform(0.01, 0.99) for i in range(layer_nodes)]  # one row
                for j in range(layer_nodes)  # for all nodes in layer (one matrix of weights)
            ]
            for k in range(layers - 1)  # for every layer
        ]

    def get_result(self, inputs):
        for input_values in inputs:
            yield self.get_final_output(input_values)[-1]

    def train(self, inputs, results):
        # results - correct answers

        for i, input_values in enumerate(inputs):
            outputs = self.get_final_output(input_values)

            # output contents final predicted result
            self.correct_weights(outputs, results[i])
            # yield outputs[-1]

    def get_final_output(self, one_input_values):
        output = one_input_values[:]

        # for every layer
        for curr_layer_index in range(self.layers - 1):
            curr_layer_weights = self.weights[curr_layer_index]
            sub_output = []

            # get output for every node
            for row in curr_layer_weights:
                sum = 0
                for item in zip(row, output):
                    sum += item[0] * item[1]

                sub_output.append(self.sigma(sum))

            # now there are outputs for current layer in sub_output
            output.append(sub_output[:])

        return output[1:]  # remove input values

    def  correct_weights(self, outputs, correct_result):
        for output in reversed(outputs):
            index = 0
            new_curr_layer_weights = []
            for o, r in zip(output, correct_result):
                if o == r:
                    index += 1
                    continue
                # for every layer
                for curr_layer_index in range(self.layers - 1, -1, -1):
                    old_curr_layer_weights = self.weights[curr_layer_index]

    def sigma(self, val):
        return 1 / (1 + exp(-1 * val))


nn = NeuralNetwork()
print(nn.train([[1, 2, 3], [3, 4, 5]], [0.4, 0.5]))
