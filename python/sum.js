function element(num) {
    sum = 0;
    for (let i = 0; i < num.length; i++) {
        ele = num[i]
        sum += num[i]
    }
    return sum;
}
num = [1, 2, 3, 4, 5]
result = element(num)
console.log(result);
