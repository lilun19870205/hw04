program main

implicit none
integer :: n
double precision, allocatable :: M(:,:), k(:),T(:)
!integer, parameter :: n=10
!double precision M(n+1,n+1)
!double precision k(n+1), T(n+1)
double precision L, A, B, C, D, E, F,dx,Q,kk
integer i,j
L=1
A=1
B=0
C=0
D=1
E=0
F=100
dx=L/n
Q=0
kk=1
n=10
write (*,*) "k="
read (*,*) kk
write (*,*) "Q="
read (*,*) Q
write (*,*) "L="
read (*,*) L
write (*,*) "n="
read (*,*) n
write (*,*) "A="
read (*,*) A
write (*,*) "B="
read (*,*) B
write (*,*) "C="
read (*,*) C
write (*,*) "D="
read (*,*) D
write (*,*) "E="
read (*,*) E
write (*,*) "F="
read (*,*) F
allocate (M(n+1,n+1))
allocate (k(n+1))
allocate (T(n+1))
do i=1,n+1
   k(i)=kk
end do
do i=1,n+1
   do j=1,n+1
      M(i,j)=0
   end do
end do

M(1,1)=(A-B/dx)
M(1,2)=B/dx
M(n+1,n)=(-E)/dx
M(n+1,n+1)=D+E/dx
do i=2,n
   M(i,i-1)=k(i)/(dx*dx)
   M(i,i)=(-1*k(i)-k(i+1))/(dx*dx)
   M(i,i+1)=k(i+1)/(dx*dx)
end do


do i=1,n+1
   write (*,204) (M(i,j),j=1,n+1)
end do
204 format (10F10.4)
!call inverse(M,M_inverse,n+1)

!do i=1,n+1
!   do j=1,n+1
!      II(i,j)=0
!      do kk=1,n+1
!         II(i,j)=II(i,j)+M(i,kk)*M_inverse(kk,j)
!      end do
!   end do
! end do
!do i=1,n+1
!   write (*,205) (II(i,j),j=1,n+1)
!end do
!205 format (12f12.6)
!call inverse(M,M_inverse,n+1)
call solve_heat_eqn(k,Q,L,n,A,B,C,D,E,F,T)



! print a header and the original matrix
  do i=1,n+1
     write (*,201) (T(i))
  end do
!do i=1,n+1
!   write (*,203) (M_inverse(i,j),j=1,n+1)
!end do
201 format (6f12.6)
!203 format (12f12.6)
end

  subroutine solve_heat_eqn(k,Q,L,n,A,B,C,D,E,F,T)
implicit none
integer n,i,j
double precision M(n+1,n+1), M_inverse(n+1,n+1)
double precision k(n+1), T(n+1), bb(n+1)
double precision L, A, B, C, D, E, F,Q
double precision dx
dx=L/n
do i=1,n+1
   do j=1,n+1
      M(i,j)=0
   end do
end do
M(1,1)=(A-B/dx)
M(1,2)=B/dx
M(n+1,n)=(-E)/dx
M(n+1,n+1)=D+E/dx
do i=2,n
   M(i,i-1)=k(i)/(dx*dx)
   M(i,i)=(-1*k(i)-k(i+1))/(dx*dx)
   M(i,i+1)=k(i+1)/(dx*dx)
end do

bb(1)=C
bb(n+1)=F
do i=2,n
   bb(i)=Q
end do

call inverse(M,M_inverse,n+1)
do i=1,n+1
   T(i)=0
   do j=1,n+1
      T(i)=T(i)+M_inverse(i,j)*bb(j)
   end do
end do
end subroutine solve_heat_eqn

  subroutine inverse(a,c,n)
!============================================================
! Inverse matrix
! Method: Based on Doolittle LU factorization for Ax=b
! Alex G. December 2009
!-----------------------------------------------------------
! input ...
! a(n,n) - array of coefficients for matrix A
! n      - dimension
! output ...
! c(n,n) - inverse matrix of A
! comments ...
! the original matrix a(n,n) will be destroyed
! during the calculation
!===========================================================
implicit none
integer n
double precision a(n,n), c(n,n)
double precision L(n,n), U(n,n), b(n), d(n), x(n)
double precision coeff
integer i, j, k

! step 0: initialization for matrices L and U and b
! Fortran 90/95 aloows such operations on matrices
L=0.0
U=0.0
b=0.0

! step 1: forward elimination
do k=1, n-1
   do i=k+1,n
      coeff=a(i,k)/a(k,k)
      L(i,k) = coeff
      do j=k+1,n
         a(i,j) = a(i,j)-coeff*a(k,j)
      end do
   end do
end do

! Step 2: prepare L and U matrices
! L matrix is a matrix of the elimination coefficient
! + the diagonal elements are 1.0
do i=1,n
  L(i,i) = 1.0
end do
! U matrix is the upper triangular part of A
do j=1,n
  do i=1,j
    U(i,j) = a(i,j)
  end do
end do

! Step 3: compute columns of the inverse matrix C
do k=1,n
  b(k)=1.0
  d(1) = b(1)
! Step 3a: Solve Ld=b using the forward substitution
  do i=2,n
    d(i)=b(i)
    do j=1,i-1
      d(i) = d(i) - L(i,j)*d(j)
    end do
  end do
! Step 3b: Solve Ux=d using the back substitution
  x(n)=d(n)/U(n,n)
  do i = n-1,1,-1
    x(i) = d(i)
    do j=n,i+1,-1
      x(i)=x(i)-U(i,j)*x(j)
    end do
    x(i) = x(i)/u(i,i)
  end do
! Step 3c: fill the solutions x(n) into column k of C
  do i=1,n
    c(i,k) = x(i)
  end do
  b(k)=0.0
end do
end subroutine inverse
