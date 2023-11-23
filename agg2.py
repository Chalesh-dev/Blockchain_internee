import numpy
import numpy as np


class aggv2:
    def __init__(self,token1_reserve, token2_reserve):
        self.token1_reserve = token1_reserve
        self.token2_reserve = token2_reserve

    def after_swap(self,token1_amount):
        new_token1_reserve = self.token1_reserve - token1_amount
        new_token2_reserve = self.token2_reserve + token1_amount
        state = state_new_reserve(new_token1_reserve, new_token2_reserve)
        return state
def state_new_reserve(new_token1_reserve, new_token2_reserve):
        return  new_token1_reserve + new_token2_reserve
def percentage(amm1 ,amm2 , token1_amount):
        percentage_range = np.linspace(0,1,100)
        states = np.zeros((len(percentage_range), len(percentage_range)))
        for i , ptc1 in enumerate(percentage_range):
            for j, ptc2 in enumerate(percentage_range):
                state_amm1 = amm1.after_swap(ptc1 *  token1_amount)
                state_amm2 = amm2.after_swap(ptc2 * token1_amount)
                total_state = state_amm1 + state_amm2
                states[i,j] = total_state
        max_indices = np.unravel_index(np.argmax(states), states.shape)
        best_amm1 = percentage_range[max_indices[0]]
        best_amm2 = percentage_range[max_indices[1]]
        best_state = states[max_indices]
        return best_amm1 , best_amm2 , best_state

amm1 = aggv2(10,50)
amm2 = aggv2(18,35)

token1_amount = 3

best_amm1, best_amm2, best_state = percentage(amm1,amm2,token1_amount)

print(token1_amount)
print(best_amm1)
print(best_amm2)
print(best_state)