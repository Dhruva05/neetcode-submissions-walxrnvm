import numpy as np
from numpy.typing import NDArray
from typing import Tuple


class Solution:
    def backward(self, x: NDArray[np.float64], w: NDArray[np.float64], b: float, y_true: float) -> Tuple[NDArray[np.float64], float]:
        # x: 1D input array
        # w: 1D weight array
        # b: scalar bias
        # y_true: true target value
        #
        # Forward: z = dot(x, w) + b, y_hat = sigmoid(z)
        # Loss: L = 0.5 * (y_hat - y_true)^2
        # Return: (dL_dw rounded to 5 decimals, dL_db rounded to 5 decimals)
        pass
        z = np.dot(w, x) + b
        y_pred = 1.0 / (1.0 + np.exp(-z))
        loss = 0.5 *(y_pred - y_true) ** 2
        grad_w = (y_pred - y_true) * (y_pred*(1-y_pred)) * x
        grad_b = (y_pred - y_true) * (y_pred*(1-y_pred))
        
        grad_w = np.round(grad_w, 5)
        grad_b = round(float(grad_b), 5)

        return (grad_w, grad_b)
