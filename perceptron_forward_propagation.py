w1 , w2 , b = 1 , 2 ,3 

def activation(x1 ,x2 ):
    z = w1 * x1 + w2 * x2 + b
    return 1 if z >= 0 else 0


def perceptron(inputs , desired_output, learning_rate , epochs):
    global w1 , w2 , b  

    for epoch in range(epochs):
        for i in range(len(inputs)):
            x1, x2 = inputs[i]
            output = activation(x1 , x2)
            error = desired_output[i] - output

            if error != 0:
                w1 += learning_rate * error * x1
                w2 += learning_rate * error * x2
                b += learning_rate * error
    return w1 , w2 , b

inputs = [(0,0) , (0,1) , (1,0) , (1,1)]
desired_output = [0 , 0 , 0 , 1]
learning_rate = 0.1
epochs = 100

w1 , w2 , b = perceptron(inputs , desired_output , learning_rate , epochs)

def test(x1, x2):
    return activation(x1 , x2)

print(test(1,1))