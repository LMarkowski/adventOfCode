const fs = require('fs');
const { parse } = require('path');

function readInput() {
    return new Promise((resolve, reject) => {
        fs.readFile('input.txt', 'utf8', (err, data) => {
            if (err) {
                console.error(err);
                reject(err);
            } else {
                const words = data.split('\n');
                resolve(words);
            }
        });
    });
}

function findFirstOccurrence(group, largerString) {
    let firstOccurrenceIndex = largerString.length; // Initialize with a value greater than any possible index

    let firstOccurrenceString = null;

    for (const str of group) {
        const index = largerString.indexOf(str);

        if (index !== -1 && index < firstOccurrenceIndex) {
            firstOccurrenceIndex = index;
            firstOccurrenceString = str;
        }
    }

    return firstOccurrenceString;
}

function findLastOccurrence(group, largerString) {
    let lastOccurrenceIndex = -1; // Initialize with a value less than any possible index

    let lastOccurrenceString = null;

    for (const str of group) {
        const index = largerString.indexOf(str);

        if (index !== -1 && index > lastOccurrenceIndex) {
            lastOccurrenceIndex = index;
            lastOccurrenceString = str;
        }
    }

    return lastOccurrenceString;
}

async function main() {
    let words;
    try {
        words = await readInput();
    } catch (err) {
        console.error(err);
    }

    let sum = 0;

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'];

    for (var word of words) {
        let tmp = 0;
        for (let i = 0; i < word.length; i++) {
            const char = word[i];
            if (numbers.includes(char)) {
                tmp += 10 * parseInt(char);
                break;
            }
        }
        for (let i = word.length - 1; i >= 0; i--) {
            const char = word[i];
            if (numbers.includes(char)) {
                tmp += parseInt(char);
                break;
            }
        }

        sum += tmp;
    }

    console.log("Part one: " + sum);

    real_numbers = {
        'one': "one1one",
        'two': "two2two",
        'three': "three3three",
        'four': "four4four",
        'five': "five5five",
        'six': "six6six",
        'seven': "seven7seven",
        'eight': "eight8eight",
        'nine': "nine9nine"
    }

    sum = 0;

    // for (const word of words) {
    //     const first = findFirstOccurrence(Object.keys(real_numbers), word);
    //     const last = findLastOccurrence(Object.keys(real_numbers), word);

    //     console.log(word);
    //     console.log(first);
    //     tmp_word = word.replace(first, real_numbers[first]);
    //     console.log(tmp_word);

    //     let tmp = 0;
    //     for (let i = 0; i < tmp_word.length; i++) {
    //         const char = tmp_word[i];
    //         if (numbers.includes(char)) {
    //             tmp += 10 * parseInt(char);
    //             break;
    //         }
    //     }

    //     tmp_word = word.replaceAll(last, real_numbers[last]);
    //     console.log(last);
    //     console.log(tmp_word);


    //     for (let i = tmp_word.length - 1; i >= 0; i--) {
    //         const char = tmp_word[i];
    //         if (numbers.includes(char)) {
    //             tmp += parseInt(char);
    //             break;
    //         }
    //     }
    //     console.log(tmp);

    //     console.log("\n");

    //     sum += tmp;
    // }

    for (const word of words) {
        let tmp_word = word;
        for (const key of Object.keys(real_numbers)) {
            if (word.includes(key)) {
                tmp_word = tmp_word.replaceAll(key, real_numbers[key]);
            }
        }
        let tmp = 0;
        for (let i = 0; i < tmp_word.length; i++) {
            const char = tmp_word[i];
            if (numbers.includes(char)) {
                tmp += 10 * parseInt(char);
                break;
            }
        }
        for (let i = tmp_word.length - 1; i >= 0; i--) {
            const char = tmp_word[i];
            if (numbers.includes(char)) {
                tmp += parseInt(char);
                break;
            }
        }
        console.log(word);
        console.log(tmp_word);
        console.log(tmp);

        sum += tmp;

    }

    console.log("Part two: " + sum);

}
main();
