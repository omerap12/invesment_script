from Omerbag import Omberbag
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} MONEY")
        exit(1)
    try:
        money = int(sys.argv[1])
    except Exception as e:
        print("Please enter valid money amount")
        print(e)
        exit(2)
    money_bag = Omberbag()
    money_bag.money_to_invest(money)