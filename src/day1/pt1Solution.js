const { INPUT } = require("./input");


function getResult(input) {
    counter = 0;
    prev = Infinity;

    for (let cur of input) {
        if (cur > prev) {
            counter++;
        }
        prev = cur;
    }

    return counter;
}

console.log(getResult(INPUT));
