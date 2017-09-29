module f90pagerank
  implicit none
  private 
  public l1norm, compute_pagerank

contains

  function l1norm(length, vec1, vec2) result(l1dist)
    integer, intent(in) :: length
    real, dimension(length), intent(in) :: vec1, vec2
    real :: l1dist
    integer :: i

    l1dist = 0.
    do i=1, length
       l1dist = l1dist + abs(vec1(i)-vec2(i))
    end do
  end function l1norm

  
  function compute_pagerank(n, A, eps, maxstep) result(r)
    integer, intent(in) :: n
    real, dimension(n, n), intent(in) :: A
    real, intent(in) :: eps
    integer, intent(in) :: maxstep
    real, dimension(n) :: r, newr
    logical :: converged
    integer :: stepid, i
    
    converged = .false.
    do i=1, n
       r(i) = 1./n
    end do
    stepid = 0

    do
       if ((converged) .or. (stepid >= maxstep)) then
          exit
       end if

       newr = matmul(A, r)
       converged = (l1norm(n, newr, r) < eps)
       r(:) = newr(:)
       stepid = stepid + 1
    end do
  end function compute_pagerank

end module f90pagerank


! compiling
! > f2py -h f90pagerank.pyf -m f90pagerank f90pagerank.f90
! > f2py -c f90pagerank.pyf f90pagerank.f90

    
     
    
