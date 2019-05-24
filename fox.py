from mpi4py import MPI
from Config import Config
import math
import sys
from array import array
import struct
from decimal import Decimal
import numpy
if len(sys.argv)<2:
    print("specify: matrixA matrixB matrixC")
    sys.exit(0)
comm = MPI.COMM_WORLD
myrank = comm.Get_rank()
nproc = comm.Get_size()



config=Config()
config.A_file=MPI.File.Open(comm,sys.argv[1])
config.B_file=MPI.File.Open(comm,sys.argv[2])
config.C_file=MPI.File.Open(comm,sys.argv[3])
config.world_rank=myrank
config.WORLD_SIZE=nproc


if config.world_rank == 0:
    ba = bytearray(2)
    config. A_file.Iread(ba)
    size = struct.unpack('<H',ba)[0]
    config.A_dims=[size,size]
    config.B_dims = [size,size]

config.A_dims=comm.bcast(config.A_dims, root=0)
config.B_dims=comm.bcast(config.B_dims, root=0)

config.dim = [math.sqrt(config.WORLD_SIZE),math.sqrt(config.WORLD_SIZE)]

wrap_around=[0,1]

config.grid_comm=comm.Create_cart(config.dim,periods=wrap_around)
config.grid_rank=config.grid_comm.Get_rank()
free_coords=[0,1]
config.row_comm=config.grid_comm.Sub(free_coords)
config.row_rank=config.row_comm.Get_rank()
free_coords=[1,0]
config.col_comm=config.grid_comm.Sub(free_coords)
config.col_rank=config.col_comm.Get_rank()

config.matrix_size= config.A_dims[0]*config.A_dims[0]
config.local_dims=[int(config.A_dims[0]/config.dim[0]),int(config.A_dims[0]/config.dim[0])]

config.local_size=int(config.local_dims[0]*config.local_dims[1])

config.coords=config.grid_comm.Get_coords(config.grid_rank)

config.my_row=config.coords[0]
config.my_col=config.coords[1]

starts = [config.my_row*int(config.local_dims[0]),config.my_col*int(config.local_dims[0])]

if config.world_rank ==2:
  print("my row and column is %d %d and %d and starts is %d %d " ,(config.my_row,config.my_col,int(config.local_dims[0]),starts[0],starts[1]))
config.block=MPI.FLOAT.Create_subarray(config.A_dims,config.local_dims, starts, order=MPI.ORDER_C)
config.block.Commit()
#config.C=[0]*config.local_size
config.A_file.Set_view(disp= MPI.INT.Get_size()*2,filetype=config.block)
config.B_file.Set_view(disp= MPI.INT.Get_size()*2,filetype=config.block)
#config.A=numpy.ndarray(int(config.local_dims[0] *config.local_dims[0]),dtype=float)
#config.B=numpy.ndarray(int(config.local_dims[0] *config.local_dims[0]),dtype=float)
#config.C=numpy.ndarray(int(config.local_dims[0] *config.local_dims[0]),dtype=float)
config.A=array('f',[0.0]*int(config.local_dims[0] *config.local_dims[0]))
config.B=array('f',[0.0]*int(config.local_dims[0] *config.local_dims[0]))
config.C=array('f',[0.0]*int(config.local_dims[0] *config.local_dims[0]))
config.A_file.Read_all(config.A)
config.B_file.Read_all(config.B)
#print(config.A)


config.A_file.Close()
config.B_file.Close()
"""
for i in range(0, int(config.local_dims[0])):
   for j in range(0, int(config.local_dims[0])):
       #config.A[int(i * config.local_dims[0] + j)]=round(config.A[int(i * config.local_dims[0] + j)],8)
       print("rank %d value %f " %(config.world_rank,config.A[int(i * config.local_dims[0] + j)]))
print("\n")     
for i in range(0, int(config.local_dims[0])):
   for j in range(0, int(config.local_dims[0])):
       #config.A[int(i * config.local_dims[0] + j)]=round(config.A[int(i * config.local_dims[0] + j)],8)
       print("rank %d value %f " %(config.world_rank,config.B[int(i * config.local_dims[0] + j)]))
print("\n")
"""  
config.compute_fox()
#if config.world_rank ==0 :
for i in range(0, int(config.local_dims[0])):
   for j in range(0, int(config.local_dims[0])):
       #config.A[int(i * config.local_dims[0] + j)]=round(config.A[int(i * config.local_dims[0] + j)],8)
       print("rank %d value %f " %(config.world_rank,config.C[int(i * config.local_dims[0] + j)]))
