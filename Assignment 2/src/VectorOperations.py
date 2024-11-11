from m5.params import *
from m5.SimObject import SimObject

class VectorOperations(SimObject):
    type = 'VectorOperations'
    cxx_header = "learning_gem5/part2/vector_operations.hh"
    cxx_class = "gem5::VectorOperations"
    
    cyclesForCrossProduct = Param.Int(150, "Cycles to Execute Event VectorCrossProduct")
    cyclesForNormalize = Param.Int(1500, "Cycles to Execute Event NormalizeVector")
    cyclesForVectorSubtraction = Param.Int(15000, "Cycles to Execute Event VectorSubtraction")
    
    arrr1 = VectorParam.Int([1, 2, 3], "Input Vector 1")
    arrr2 = VectorParam.Int([4, 5, 6], "Input Vector 2")
