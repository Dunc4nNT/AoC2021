const { INPUT } = require("./input");


function getResult(input) {
    let horizontal = 0;
    let depth = 0;

    for (line of input) {
        let lineArray = line.split(" ");
        let direction = lineArray[0];
        let value = parseInt(lineArray[1]);

        if (direction === "forward") {
            horizontal += value;
        } else if (direction === "down") {
            depth += value;
        } else if (direction === "up") {
            depth -= value;
        }
    }

    return horizontal * depth;
}


console.log(getResult(INPUT));
