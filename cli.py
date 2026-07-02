import argparse
from bot.client import BinanceFuturesClient

API_KEY = "4MJlSQqtKGnWLF5MpvrbV01GnIrwIdsGKRuNIu6L8iu6y7S4SKLmUYNaYwGVJlo7"
API_SECRET = "HdP6kt8CBXlMtBANqJ555NLcQ0lq7L38FNRozLObIWpNBks608UYrobNJDUmeu2N"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--symbol', required=True)
    parser.add_argument('--side', required=True)
    parser.add_argument('--type', required=True)
    parser.add_argument('--qty', type=float, required=True)
    
    args = parser.parse_args()
    
    bot = BinanceFuturesClient(API_KEY, API_SECRET)
    order = bot.place_order(args.symbol, args.side, args.type, args.qty)
    print("Success! Order Details:", order)

if __name__ == "__main__":
    main()