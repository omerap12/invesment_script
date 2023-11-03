from Omerbag import Omberbag
import sys
import argparse

if __name__ == "__main__":
    money_bag = Omberbag()
    parser = argparse.ArgumentParser()
    parser.add_argument('-m',"--MONEY", help="Amount of money to invest in eash security", type=int)
    parser.add_argument('-info',"--INFO", help="Show securities info", action='store_true')
    args = parser.parse_args()
    
    if args.MONEY:
        money_bag.money_to_invest(args.MONEY)
    if args.INFO:
        money_bag.print_securities()