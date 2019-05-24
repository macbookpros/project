#include <stdio.h>
#include <stdlib.h>
#include <cblas.h>
void matmul(float**, float**, float**, int);
int main(int argc, char *argv[])
{
	if (argc < 6) {
		printf("Usage: %s [M] [K] [N] [output A] [output B] [output Answer] [seed]\n");
		exit(1);
	}

	if (argc == 8) {
		srand(atoi(argv[7]));
	}

	int A_dims[] = {atoi(argv[1]), atoi(argv[2])};
	int B_dims[] = {atoi(argv[2]), atoi(argv[3])};
	float *A = (float*)malloc(sizeof(float) * (A_dims[0] * A_dims[1]));
	float *B = (float*)malloc(sizeof(float) * (B_dims[0] * B_dims[1]));
	float *C = (float*)malloc(sizeof(float) * (A_dims[0] * B_dims[1]));
	//double *C_test = (double*)malloc(sizeof(double) * (A_dims[0] * B_dims[1]));
       int i,j,k;
	for (i = 0; i < A_dims[0] * A_dims[1]; i++) {
		A[i] = (float)rand() / (float)RAND_MAX;
               // printf("%lf\n",A[i]);
	}
	for (i = 0; i < B_dims[0] * B_dims[1]; i++) {
		B[i] = (float)rand() / (float)RAND_MAX;
              //printf("%lf\n",B[i]);
	}
        /*
         for (i = 0; i < A_dims[0] * B_dims[1]; i++)
          {
            for (j = 0; i < A_dims[0] * B_dims[1]; i++) 
           {
              for (k = 0; k < A_dims[0] * B_dims[1]; k++)
              {  
              C[i*A_dims[0]+j] += A[i*A_dims[0]+k]*B[k*A_dims[0]+j];
              }
           }
           }
          for (i = 0; i < A_dims[0] * B_dims[1]; i++) {
              printf("%f\n",C[i]);
        }*/
     // matmul(&A,&B,&C,A_dims[0]);
   
	/*cblas_dgemm(CblasRowMajor, CblasNoTrans, CblasNoTrans,
                                        A_dims[0], B_dims[1], A_dims[1],
                                        1.0, A, A_dims[1], B, B_dims[1],
                                        0.0, C, B_dims[1]);
*/
	FILE *file = fopen(argv[4], "wb");
	fwrite(A_dims, sizeof(int), 2, file);
	fwrite(A, sizeof(float), A_dims[0] * A_dims[1], file);
	fclose(file);

	file = fopen(argv[5], "wb");
	fwrite(B_dims, sizeof(int), 2, file);
	fwrite(B, sizeof(float), B_dims[0] * B_dims[1], file);
	fclose(file);
/*       
	file = fopen(argv[6], "wb");
	fwrite(&A_dims[0], sizeof(int), 1, file);
	fwrite(&B_dims[1], sizeof(int), 1, file);
	fwrite(C, sizeof(float), A_dims[0] * B_dims[1], file);
	fclose(file);
*/
    // for (i = 0; i < B_dims[0] * B_dims[1]; i++) {
               // B[i] = (float)rand() / (float)RAND_MAX;
      //        printf("%lf\n",C[i]);
       // }
}
void matmul(float **a, float **b, float **c, int size)
{
        int i,j,k;

        float **temp = (float**) malloc(size*sizeof(float*));
        for(i=0;i<size;i++)
                *(temp+i)=(float*) malloc(size*sizeof(float));

        for(i=0;i<size;i++)
        {
                        for(j=0;j<size;j++)
                        {
                                temp[i][j]=0;
                                for(k=0;k<size;k++){
                                        temp[i][j]=temp[i][j]+ (a[i][k] * b[k][j]);
                                }
                        }
        }

        for(i=0;i<size;i++)
                for(j=0;j<size;j++)
                        c[i][j]+=temp[i][j];

}

