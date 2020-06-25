bubbleSort <- function(arr) {
  n = length(arr) 
  for (i in 1:(n-1)) {
    print(arr)
    for (j in 1:(n-i)) {
      if (arr[j] > arr[j+1]) {
        copy = arr[j]
        arr[j] = arr[j+1]
        arr[j+1] = copy
      }
    }
  }
  print(arr)
  return(arr)
}