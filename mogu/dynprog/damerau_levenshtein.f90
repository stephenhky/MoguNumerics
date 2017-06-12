module demarau_levenshtein
implicit none
private
public damarau_levenshtein_distance

contains

integer function damarau_levenshtein_distance(word1, word2) result(dldist)
  character(len=*), intent(in) :: word1, word2
  integer :: len1, len2, i, j, delcost, inscost, unequalcost, subscost, transcost
  integer, dimension(:, :), allocatable :: matrix

  len1 = len(word1)
  len2 = len(word2)
  allocate(matrix(len1, len2))

  do i = 1, len1
     do j = 1, len2
        if (min(i, j)==1) then
           matrix(i, j) = max(i-1, j-1)
        else
           unequalcost = 1
           if (word1(i)==word2(j)) unequalcost = 0

           delcost = matrix(i-1, j) + 1
           inscost = matrix(i, j-1) + 1
           subscost = matrix(i-1, j-1) + unequalcost

           if (i>2 .and. j>2 .and. word1(i)==word2(j-1) .and. word1(i-1)==word2(j)) then
              transcost = matrix(i-2, j-2) + unequalcost
              matrix(i, j) = min(delcost, inscost, subscost, transcost)
           else
              matrix(i, j) = min(delcost, inscost, subscost)
           end if
        end if
     end do
  end do

  dldist = matrix(len1, len2)
  
  deallocate(matrix)
  
end function

end module
