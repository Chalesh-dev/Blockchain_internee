from amm_pool import AMM_pool


class agg_pool():
    def __init__(self, dex_list):
        self.dex_list = dex_list
    def swap_sim(self,amount_in_0,amount_in_1):
            item_list = []

            for item in self.dex_list:
                    item_list.append(item.simulate(amount_in_0 , amount_in_1))
            index_high = item_list.index(max(item_list))

            if amount_in_1 != 0:
                self.dex_list[index_high].swap(token_2_in=amount_in_1)
            elif amount_in_0 != 0:
                self.dex_list[index_high].swap(token_1_in=amount_in_0)

amm1 = AMM_pool(7,6)
amm2 = AMM_pool(10,13)
amm3 = AMM_pool(11,17)
amm4 =AMM_pool(8,9)
amm5 =AMM_pool(5,4)
amm6 =AMM_pool(8,6)


print(amm1.get_token1())
print(amm2.get_token1())
print(amm3.get_token1())
print(amm4.get_token1())
print(amm5.get_token1())
print(amm6.get_token1())
print()
print()
agg1 = agg_pool([amm1 , amm2 , amm3])
agg2 = agg_pool([amm4 , amm5 , amm6])
agg1.swap_sim(12 , 0)
agg2.swap_sim(13,0)
print(amm1.get_token1())
print(amm2.get_token1())
print(amm3.get_token1())
print(amm4.get_token1())
print(amm5.get_token1())
print(amm6.get_token1())
