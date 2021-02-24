import argparse
import functions

parser=argparse.ArgumentParser()
parser.add_argument("x",type=int,help='votre nombre')
args=parser.parse_args()

print(functions.racine_carree(args.x))
