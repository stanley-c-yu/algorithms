const bubbleSort = (arr) => {
    let n = arr.length;
    for (let i = 0; i < n; i++) {
        console.log(arr);
        for (let j = 0; j < (n-i-1); j++) {
            if (arr[j] > arr[j+1]) {
                let copy = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = copy;
            }
        }
    }
    console.log(arr);
    return arr;
}

console.log("Partially Sorted Array Test: ");  
let sorted_arr_1 = bubbleSort([33, 166, 5, 23, 3.14]);

console.log("Reverse Sorted Array Test: ");
let sorted_arr_2 = bubbleSort([500, 266, 69, 28, 13]);
