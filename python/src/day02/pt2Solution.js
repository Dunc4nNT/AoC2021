const { INPUT } = require("./input");


function getResult(input) {
    let horizontal = 0;
    let depth = 0;
    let aim = 0;

    for (line of input) {
        let lineArray = line.split(" ");
        let direction = lineArray[0];
        let value = parseInt(lineArray[1]);

        if (direction === "forward") {
            horizontal += value;
            depth += aim * value;
        } else if (direction === "down") {
            aim += value;
        } else if (direction === "up") {
            aim -= value;
        }
    }

    return horizontal * depth;
}


console.log(getResult(INPUT));
