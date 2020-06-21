let bubbleSort = (arr) => {
    let len = arr.length;
    for (let i = 0; i < len; i++) {
        console.log(arr);
        for (let j = 0; j < (len-i); j++) {
            if (arr[j] > arr[j+1]) { 
                let copy = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = copy;
            }
        }
    }
    return arr;
}

bubbleSort([30,25,45,60,8])