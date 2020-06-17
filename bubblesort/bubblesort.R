bubbleSort <- function(array) {
  n = length(array);
  for (i in 1:(n-1)) {
    print(array);
    for (j in 1:(n-i)) {
      if(array[j] > array[j+1]) {
        copy = array[j];
        array[j] = array[j+1];
        array[j+1] = copy;
      }
    }
  }
  print(array)
  return(array)
}

#bubbleSort(c(5,4,3,2,1))
