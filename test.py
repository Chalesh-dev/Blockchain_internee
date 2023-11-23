import numpy as np

class AMMPool:
    def __init__(self, token1_reserve, token2_reserve):
        self.token1_reserve = token1_reserve
        self.token2_reserve = token2_reserve

    def calculate_state(self, percentage_token1):
        total_tokens = self.token1_reserve + self.token2_reserve
        tokens_to_provide = total_tokens * percentage_token1

        new_token1_reserve = self.token1_reserve - tokens_to_provide
        new_token2_reserve = self.token2_reserve + tokens_to_provide

        # Assume some logic to calculate the state based on new reserves
        state = calculate_state_logic(new_token1_reserve, new_token2_reserve)

        return state

def calculate_state_logic(new_token1_reserve, new_token2_reserve):

    return new_token1_reserve + new_token2_reserve

def optimize_state(amm1, amm2, percentage_range):

    states = np.zeros((len(percentage_range), len(percentage_range)))

    for i, pct1_amm1 in enumerate(percentage_range):
        for j, pct1_amm2 in enumerate(percentage_range):
            state_amm1 = amm1.calculate_state(pct1_amm1)
            state_amm2 = amm2.calculate_state(pct1_amm2)
            total_state = state_amm1 + state_amm2
            states[i, j] = total_state

    max_indices = np.unravel_index(np.argmax(states), states.shape)
    best_percentage_amm1 = percentage_range[max_indices[0]]
    best_percentage_amm2 = percentage_range[max_indices[1]]
    best_state = states[max_indices]

    return best_percentage_amm1, best_percentage_amm2, best_state

# Example Usage:
amm1 = AMMPool(50, 50)
amm2 = AMMPool(50, 50)

percentage_range = np.linspace(0, 1, 100)  # Range of percentages to test

best_percentage_amm1, best_percentage_amm2, best_state = optimize_state(amm1, amm2, percentage_range)

# Print the results
print(f"Best Distribution of Funds:")
print(f"AMM1: {best_percentage_amm1 * 100}%")
print(f"AMM2: {best_percentage_amm2 * 100}%")
print(f"Maximized State: {best_state}")
