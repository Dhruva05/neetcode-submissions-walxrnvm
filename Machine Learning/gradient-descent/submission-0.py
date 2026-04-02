class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places
        pass

        x_val = init

        for i in range(iterations):
            #f(x) = 2*x = 2 *x_val
            derivative = 2*x_val

            x_val = x_val - (derivative*learning_rate)
        
        return round(x_val, 5)
