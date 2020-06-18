bubbleSort <- function(arr) { 
  n = length(arr)
  for (i in 1:n) {
    print(arr)
    for (j in 1:(n-1)) {
      if (arr[j] > arr[j+1]) {
        copy = arr[j]
        arr[j] = arr[j+1]
        arr[j+1] = copy
      }
    }
  }
  return(arr)
}