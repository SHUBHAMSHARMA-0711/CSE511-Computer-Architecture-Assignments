#include <cmath>
#include <vector>
#include "base/trace.hh"
#include "debug/VECTOR.hh"
#include "debug/NORMALIZE.hh"
#include "debug/RESULTSUB.hh"
#include "debug/RESULTCROSS.hh"
#include "learning_gem5/part2/vector_operations.hh"

namespace gem5
{

VectorOperations::VectorOperations(const VectorOperationsParams &parameter) : 
	SimObject(parameter), 
	arrrr1(parameter.arrr1),
	arrrr2(parameter.arrr2),
	cyclesForCrossProductt(parameter.cyclesForCrossProduct),
	cyclesForNormalizee(parameter.cyclesForNormalize),
	cyclesForVectorSubtractionn(parameter.cyclesForVectorSubtraction),
	VectorCrossProduct([this]{function_VectorCrossProduct();}, name()),
	NormalizeVector([this]{function_NormalizeVector();}, name()),
	VectorSubtraction([this]{function_VectorSubtraction();}, name())
	
{
    arr1[0][0] = arrrr1[0];
    arr1[1][0] = arrrr1[1];
    arr1[2][0] = arrrr1[2];
    arr2[0][0] = arrrr2[0];
    arr2[1][0] = arrrr2[1];
    arr2[2][0] = arrrr2[2];
    
    DPRINTF(VECTOR, "Input Vectors:-\n");
    DPRINTF(VECTOR, "Vector A:- {%d, %d, %d}\n", arr1[0][0], arr1[1][0], arr1[2][0]);
    DPRINTF(VECTOR, "Vector B:- {%d, %d, %d}\n", arr2[0][0], arr2[1][0], arr2[2][0]);
}

void
VectorOperations::function_VectorCrossProduct()
{
    DPRINTF(RESULTCROSS, "Cross Product of Vector A and Vector B is:- {%d, %d, %d}\n", (arr1[1][0] * arr2[2][0]) - (arr1[2][0] * arr2[1][0]), (arr1[2][0] * arr2[0][0]) - (arr1[0][0] * arr2[2][0]), (arr1[0][0] * arr2[1][0]) - (arr1[1][0] * arr2[0][0]));
}

void
VectorOperations::function_NormalizeVector()
{
    int mag1 = (arr1[0][0] * arr1[0][0]) + (arr1[1][0] * arr1[1][0]) + (arr1[2][0] * arr1[2][0]);
    int mag2 = (arr2[0][0] * arr2[0][0]) + (arr2[1][0] * arr2[1][0]) + (arr2[2][0] * arr2[2][0]);
    
    DPRINTF(NORMALIZE, "Normalization of Vector A is:- {%d, %d, %d}\n", arr1[0][0] / sqrt(mag1), arr1[1][0] / sqrt(mag1), arr1[2][0] / sqrt(mag1));
    DPRINTF(NORMALIZE, "Normalization of Vector B is:- {%d, %d, %d}\n", arr2[0][0] / sqrt(mag2), arr2[1][0] / sqrt(mag2), arr2[2][0] / sqrt(mag2));
}

void
VectorOperations::function_VectorSubtraction()
{
    DPRINTF(RESULTSUB, "Subtraction of Vector A and Vector B is:- {%d, %d, %d}\n", arr1[0][0] - arr2[0][0], arr1[1][0] - arr2[1][0], arr1[2][0] - arr2[2][0]);
}

void
VectorOperations::startup()
{
    schedule(VectorCrossProduct , cyclesForCrossProductt);
    schedule(NormalizeVector   , cyclesForNormalizee);
    schedule(VectorSubtraction, cyclesForVectorSubtractionn);
}

} // namespace gem5
