const { INPUT } = require("./input");


function getOxyGenRating(input) {
    let oxyGenRating;
    let valuesLeft = input;

    for (let i = 0; i <= input[0].length; i++) {
        let valuesStarting0 = [];
        let valuesStarting1 = [];

        for (value of valuesLeft) {
            if (value[i] === "0") {
                valuesStarting0.push(value);
            } else {
                valuesStarting1.push(value);
            }
        }

        if (valuesStarting1.length >= valuesStarting0.length) {
            valuesLeft = valuesStarting1;
        } else {
            valuesLeft = valuesStarting0;
        }

        if (valuesLeft.length == 1) {
            oxyGenRating = valuesLeft[0];
            break;
        }
    }
    return parseInt(oxyGenRating, 2);
}

function getCo2ScrubberRating(input) {
    let Co2ScrubberRating;
    let valuesLeft = input;

    for (let i = 0; i <= input[0].length; i++) {
        let valuesStarting0 = [];
        let valuesStarting1 = [];

        for (value of valuesLeft) {
            if (value[i] === "0") {
                valuesStarting0.push(value);
            } else {
                valuesStarting1.push(value);
            }
        }

        if (valuesStarting1.length < valuesStarting0.length) {
            valuesLeft = valuesStarting1;
        } else {
            valuesLeft = valuesStarting0;
        }

        if (valuesLeft.length == 1) {
            Co2ScrubberRating = valuesLeft[0];
            break;
        }
    }

    return parseInt(Co2ScrubberRating, 2);
}


function getResult(input) {
    let oxyGenRating = getOxyGenRating(input);
    let Co2ScrubberRating = getCo2ScrubberRating(input);

    return oxyGenRating * Co2ScrubberRating;
}


console.log(getResult(INPUT));
