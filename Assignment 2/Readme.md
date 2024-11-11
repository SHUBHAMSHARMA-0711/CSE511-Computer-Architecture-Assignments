# Making GEM5 custom SimObject: VectorOperations

Our Custom SimObject called __"VectorOperations"__ which will call three events, namely, __VectorCrossProduct__, __NormalizeVector__, and __VectorSubtraction__.
Initially these events will be called at tick 150, 1500, 15000 respectively. But later on we modifies our config file (`script.py`) and allowed user to provide input ticks as a parameter.

## File Descriptions

1. `VectorOperations.py`:
   - Main Python file in which our SimObject class `VectorOperations` is defined.
   - It specifies various parameters and attributes that takes user input for `ticks` and `vectors`.

2. `vector_operations.hh`:
   - This C++ header file will contains the class declaration for `VectorOperations`.
   - It consists of one public constructor, three private EventFunctionWrapper and three fucntions for three different vector opreations.

3. `vector_operations.cc`:
   - This C++ source file will implement the fucntions and constructor defined in `vector_operations.hh`.
   - The `DPRINTF` macro is used for debugging and printing simulation results using different Debug flags.

4. `SConscript`:
   - The `SConscript` file is used for configuring the build process of the Gem5 simulation.
   - It is the file in which all 4 Debug flags(`VECTOR`, `RESULTCROSS`, `NORMALIZE`, `RESULTSUB`) are declared and defined.

5. `script.py`:
   - This simple Python script is used to run and control the Gem5 simulation.
   - By importing `argparse` libraray I enabled user to provide custom arguments such as cycle counts and input vectors through command-line arguments. 

## Steps for Compiling and Running files

1. First `cd` into `gem5` folder.
2. Rebuild `gem5` after modifying files in the `src/learning_gem5` folder.
3. After rebuilding if you want to run simulations on default parameters then run the below command.

   ```shell
   build/X86/gem5.opt --debug-flags=VECTOR,RESULTCROSS,NORMALIZE,RESULTSUB /home/shubham21099/CA/Assignment_2/script.py
   ```
4. If you want to run simulation by passing parameters through command line then use below command.

   ```shell
   build/X86/gem5.opt --debug-flags=VECTOR,RESULTCROSS,NORMALIZE,RESULTSUB /home/shubham21099/CA/Assignment_2/script.py --crossProduct 500 --normalize 5000 --vectorSubtraction 50000 --vector1 4 5 6 --vector2 1 2 3
   ```

