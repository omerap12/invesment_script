class Omberbag:
    def __init__(self) -> None:
        self.securities = {'1159250':'S&P500','1159094':'SMEA','1159169':'EIMI'}
        self.precentage = {'1159250': 0.6, '1159094':0.25, '1159169': 0.15}
    
    def money_to_invest(self,quantity: int) -> int:
        for item in self.securities.keys():
            print(f'{item} ---> {int(self.precentage[item]*quantity)}')

    def print_securities(self) -> str:
        print("".join(f"{key}: {value}\n" for key,value in self.securities.items()))
