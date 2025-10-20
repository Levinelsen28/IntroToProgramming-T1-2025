#code wars
def odd_or_even(arr):
  """
  Determines if the sum of elements in a list of integers is odd or even.
  An empty list is considered as [0].
  """
  # The sum of an empty list is 0 by default, which is even.
  # So we can just use sum() without an extra check.
  sum_of_elements = sum(arr)
  
  # Check if the sum is perfectly divisible by 2.
  if sum_of_elements % 2 == 0:
    return "even"
  else:
    return "odd"
