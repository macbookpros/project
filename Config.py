#import numpy
from mpi4py import MPI
from array import array
class Config:
    A_file = None
    B_file = None
    C_file = None
    grid_comm = None
    row_comm = None
    col_comm = None
    dim = []
    coords = []
    A_dims = array('i',[0]*2)
    B_dims = array('i',[0]*2)
    C_dims = array('i',[0]*2)
    matrix_size = 0
    local_dims = []
    local_size = 0
    my_row = 0
    my_col = 0
    world_rank=None
    WORLD_SIZE=None
    grid_rank=None
    A=None
    A_tmp=None
    B=None
    C=None




    def compute_fox(self):
        self.A_tmp=array('f',[0.0]*int(self.local_dims[0] *self.local_dims[0]))
      #  self.A_tmp = numpy.ndarray(int(self.local_dims[0] *self.local_dims[0]*8))
        source = (self.my_row + 1) % int(self.dim[0])
        dest = (self.my_row + int(self.dim[0]) - 1) % int(self.dim[0])
#        print("my row is %d " %(self.my_row))
        for i in range(0,int(self.dim[0])):
            root = int((self.my_row + i) % int(self.dim[0]))
            if int(root) == int(self.my_col):
               # print("A is {}\n".format(self.A));
		self.A=self.row_comm.bcast(self.A, root)
                self.multiply_matrix(self.A)

            else:
                self.A_tmp=self.row_comm.bcast(self.A_tmp, root)
                self.multiply_matrix(self.A_tmp)

            self.col_comm.Sendrecv_replace(self.B,dest,0,source,0,status=None)


    def multiply_matrix(self, Amatrix):

        for i in range(0, int(self.local_dims[0])):
            for k in range(0, int(self.local_dims[0])):
                for j in range(0, int(self.local_dims[0])):
                    #print("A for rank {}  is {}\n".format(self.world_rank,Amatrix));
                    #print("B for rank {}  is {}\n".format(self.world_rank,self.B));
                    #print(self.C[int(i*self.local_dims[0]+j)])
                    #print(Amatrix[int(i*self.local_dims[0]+k)]*self.B[int(k*self.local_dims[0]+j)])
                    self.C[int(i*int(self.local_dims[0])+j)] += Amatrix[int(i*int(self.local_dims[0])+k)]*self.B[int(k*int(self.local_dims[0])+j)]

