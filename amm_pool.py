class AMM_pool:
    def __init__(self, token1, token2):
        self.__token1 = token1
        self.__token2 = token2
        self.__ratio = self.__token1 / self.__token2

    def k(self):
        return self.__token1 * self.__token2
    def get_token1(self):
        return self.__token1

    def get_token2(self):
        return self.__token2

    # def get_k_val(self):
    #     return self.__k

    def __swap_token1(self,amount_in):
        token2 = self.k() / (self.__token1 + amount_in)
        amount_out = self.__token2 - token2
        self.__token2 = token2
        self.__token1 += amount_in
        return amount_out
    def __swap_token2(self ,amount_in):
        token1 = self.k()/(self.__token2+amount_in)
        amount_out = self.__token1 - token1
        self.__token1 = token1
        self.__token2 += amount_in
        return amount_out
    def swap(self,**kwargs):
        try:
            self.__swap_token1(kwargs['token_1_in'])
        except:
            self.__swap_token2(kwargs['token_2_in'])

    def LP(self,amount_token1 , amount_token2):
        ratio = self.__token1/self.__token2
        if amount_token1 == 0 or amount_token2 == 0:
            raise Exception
        elif amount_token1/amount_token2 == ratio:
            self.__token1 += amount_token1
            self.__token2 += amount_token2
        else:
            ratio_input = amount_token1 / amount_token2
            if ratio_input > ratio:
                amount_token1 = self.__ratio * amount_token2
                self.__token1 += amount_token1
                self.__token2 += amount_token2
            else:
                amount_token2 = self.__ratio * amount_token1
                self.__token1 += amount_token1
                self.__token2 += amount_token2
    def simulate(self,amount_in1 = 0 , amount_in2 = 0):
        if amount_in1 == 0 :
            token1 = self.k() / (self.__token2 + amount_in2)
            amount_out = self.__token1 - token1
            return amount_out
        elif amount_in2 == 0 :
            token2 = self.k() / (self.__token1 + amount_in1)
            amount_out = self.__token2 - token2
            return amount_out
        else:
            raise

# amm1 = AMM_pool(12,5)
# print("token 1",amm1.get_token1())
# print("token2",amm1.get_token2())
# print("k",amm1.k())
