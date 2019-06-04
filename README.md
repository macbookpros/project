# project

For running python codes on beskow-
1)Login to beskow &nbsp;
 2)Allocate required nodes &nbsp;
 Type following commands- &nbsp;
 3)module load anaconda/py27/5.3 &nbsp;
 4)source activate mpi4py &nbsp;
 5)export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CONDA_PREFIX/lib &nbsp;
 To run code- &nbsp;
 aprun -n 9 python <name_of_python_file>.py <arguments> &nbsp;

For running map-
1)module load allinea-forge/18.1.1 &nbsp;
2)export ALLINEA_SAMPLER_INTERVAL=1 &nbsp;
3)map --profile aprun -n 9 python <name_of_python_file>.py <arguments> &nbsp;

Performance_source folder consists of all the code files for evaluation of basic MPI calls-
For running - broadcast.py,one-sidedcomm.py,sr_comparision.py,sr_normal.py,sr_numpy.py,user_def_type.py
aprun -n <number of processors> python <name_of_python_file>.py <size argument>
For other programs-
aprun -n <number of processors> python <name_of_python_file>.py

Fox folder consists of source files for fox algorithm-
For generating matrice elements-
1)cc generate.c &nbsp;
2)aprun ./a.out 576 576 576 A.bin B.bin C.answer 944 &nbsp;
For running - &nbsp;
aprun -n <number_of_processors> python <name_of_the_file>.py A.bin B.bin C2.answer &nbsp;
For verifying- &nbsp;
1)cc verify.c &nbsp;
2)aprun ./a.out C2.answer C.answer &nbsp;

Map folder consists of all the map files. They can be viewed using the ARM map tool.

Results Folder consists of all the table data .

