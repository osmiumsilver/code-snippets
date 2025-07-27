import numpy as np
from diffprivlib import mechanisms as mech
from diffprivlib.tools import mean, var

class DifferentialPrivacyGrid:
    def __init__(self, epsilon=1.0, delta=0.1):
        self.epsilon = epsilon
        self.delta = delta

    def add_noise_to_result(self, result, sensitivity):
        # Use Gaussian mechanism for differential privacy
        gaussian = mech.GaussianAnalytic(epsilon=self.epsilon, delta=self.delta, sensitivity=sensitivity)
        return gaussian.randomise(result)

    def private_mean(self, data):
        return mean(data, epsilon=self.epsilon)

    def private_variance(self, data):
        return var(data, epsilon=self.epsilon)

    def simulate_grid_computation(self, data, computation_type='mean'):
        if computation_type == 'mean':
            return self.private_mean(data)
        elif computation_type == 'variance':
            return self.private_variance(data)
        else:
            raise ValueError("Unsupported computation type")

# Example usage
if __name__ == "__main__":
    # Simulate some sensitive data
    sensitive_data = np.random.rand(1000) * 100  # 1000 datapoints between 0 and 100

    # Create our differential privacy wrapper
    dp_grid = DifferentialPrivacyGrid(epsilon=0.1)  # Stricter privacy

    # Simulate grid computations
    private_mean = dp_grid.simulate_grid_computation(sensitive_data, 'mean')
    private_variance = dp_grid.simulate_grid_computation(sensitive_data, 'variance')

    print(f"Private Mean: {private_mean}")
    print(f"Private Variance: {private_variance}")

    # Compare with non-private results
    print(f"Actual Mean: {np.mean(sensitive_data)}")
    print(f"Actual Variance: {np.var(sensitive_data)}")

# You can run this multiple times to see how the private results vary due to added noise