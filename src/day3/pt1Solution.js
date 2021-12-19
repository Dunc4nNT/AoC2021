const { INPUT } = require("./input");


function getResult(input) {
    let gammaRate = "";
    let epsilonRate = "";
    let bitSums = [];

    for (let value of input) {
        for (let i = 0; i < value.length; i++) {
            if (value[i] === "1") {
                bitSums[i] = (bitSums[i] || 0) + 1;
            }
        }
    }

    let halfInputLen = input.length / 2;
    for (let sum of bitSums) {
        if (sum > halfInputLen) {
            gammaRate += "1";
            epsilonRate += "0";
        } else if (sum < halfInputLen) {
            gammaRate += "0";
            epsilonRate += "1";
        }
    }

    let gammaRateDec = parseInt(gammaRate, 2);
    let epsilonRateDec = parseInt(epsilonRate, 2);

    return gammaRateDec * epsilonRateDec;
}


console.log(getResult(INPUT));
