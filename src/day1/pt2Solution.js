const { INPUT } = require("./input");

function getResult(input) {
    counter = 0;
    prev = Infinity;

    for (i = 0; i < input.length; i++) {
        let cur = input[i] + input[i+1] + input[i+2];
        if (cur > prev) {
            counter++;
        }

        prev = cur;
    }

    return counter;
}

console.log(getResult(INPUT));
