# project

For running python codes on beskow-
1)Login to beskow\n
2)Allocate required nodes
Type following commands-
3)module load anaconda/py27/5.3
4)source activate mpi4py
5)export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CONDA_PREFIX/lib
To run code-
aprun -n 9 python <name_of_python_file>.py <arguments>

For running map-
1)module load allinea-forge/18.1.1
2)export ALLINEA_SAMPLER_INTERVAL=1
3)map --profile aprun -n 9 python <name_of_python_file>.py <arguments>

Performance_source folder consists of all the code files for evaluation of basic MPI calls-
For running - broadcast.py,one-sidedcomm.py,sr_comparision.py,sr_normal.py,sr_numpy.py,user_def_type.py
aprun -n <number of processors> python <name_of_python_file>.py <size argument>
For other programs-
aprun -n <number of processors> python <name_of_python_file>.py

Fox folder consists of source files for fox algorithm-
For generating matrice elements-
1)cc generate.c
2)aprun ./a.out 576 576 576 A.bin B.bin C.answer 944
For running -
aprun -n <number_of_processors> python <name_of_the_file>.py A.bin B.bin C2.answer
For verifying-
1)cc verify.c
2)aprun ./a.out C2.answer C.answer

Map folder consists of all the map files. They can be viewed using the ARM map tool.

Results Folder consists of all the table data .

