const bubbleSort = (arr) => {
    const n = arr.length;
    for (let i = 0; i < n; i++) {
        console.log(arr); 
        for (let j = 0; j < (n-i); j++) {
            if (arr[j] > arr[j+1]) {
                let copy = arr[j]; 
                arr[j] = arr[j+1];
                arr[j+1] = copy;
            }
        }
    }
    return arr;
}

bubbleSort([33, 166, 5, 23, 3.14])