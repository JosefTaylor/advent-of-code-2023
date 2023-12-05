program day_01A

implicit none

write(*,*) 'one2three4five'
write(*,*) first_last('one2three4five')

contains

function first_last(line) result(out)
character(*), intent(in) :: line
integer :: out

integer :: i, loc, count
character(20) :: numbers
character(len=2) :: text

i = 1
count = 0
numbers = ''
write(*,*) "starting"
do while (i < len_trim(line))
  write(*,*) line(i:)
  loc = scan(line(i:), '123456789')
  if (loc /= 0) then
    i = i + loc
    count = count + 1
    numbers(count:count) = line(loc:loc)
  else
    exit
  end if
end do

text = numbers(1:1) // numbers(len_trim(numbers):len_trim(numbers))
write(*,*) numbers
! read(text,*) out

out = 11

end function

end program