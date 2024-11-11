#ifndef __MAKING_GEM5_VECTOR_OPERATIONS_HH__
#define __MAKING_GEM5_VECTOR_OPERATIONS_HH__

#include <vector>
#include "sim/sim_object.hh"
#include "params/VectorOperations.hh"

namespace gem5
{

class VectorOperations : public SimObject
{
  private:
    int arr1[3][1] = {{1}, {2}, {3}};
    int arr2[3][1] = {{4}, {5}, {6}};
    
    std::vector<int> arrrr1;
    std::vector<int> arrrr2;
    
    int cyclesForCrossProductt;
    int cyclesForNormalizee;
    int cyclesForVectorSubtractionn;
    
    void function_VectorCrossProduct();
    void function_NormalizeVector();
    void function_VectorSubtraction();
    
    EventFunctionWrapper VectorCrossProduct;
    EventFunctionWrapper NormalizeVector;
    EventFunctionWrapper VectorSubtraction;

  public:
    VectorOperations(const VectorOperationsParams &parameter);
    
    void startup() override;
};

}

#endif // __MAKING_GEM5_VECTOR_OPERATIONS_HH__
