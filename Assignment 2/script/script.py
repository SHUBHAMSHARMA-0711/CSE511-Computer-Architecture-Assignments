import m5
from m5.objects import *
import argparse

parser = argparse.ArgumentParser(description="SimObject VectorOperations Simulation")
parser.add_argument("--crossProduct", type=int, default=150, help="Cycles to Execute Event VectorCrossProduct")
parser.add_argument("--normalize", type=int, default=1500, help="Cycles to Execute Event NormalizeVector")
parser.add_argument("--vectorSubtraction", type=int, default=15000, help="Cycles to Execute Event VectorSubtraction")
parser.add_argument("--vector1", nargs='+', type=int, default=[1, 2, 3], help="Input Vector 1")
parser.add_argument("--vector2", nargs='+', type=int, default=[4, 5, 6], help="Input Vector 2")

root = Root(full_system=False)
root.vector = VectorOperations()

root.vector.cyclesForCrossProduct = parser.parse_args().crossProduct
root.vector.cyclesForNormalize = parser.parse_args().normalize
root.vector.cyclesForVectorSubtraction = parser.parse_args().vectorSubtraction
root.vector.arrr1 = parser.parse_args().vector1
root.vector.arrr2 = parser.parse_args().vector2

m5.instantiate()

print("Beginning simulation!")
exit_event = m5.simulate()
print('Exiting @ tick {} because {}'.format(m5.curTick(), exit_event.getCause()))
