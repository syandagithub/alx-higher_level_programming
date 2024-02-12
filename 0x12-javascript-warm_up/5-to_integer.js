#!/usr/bin/node

const firstArg = process.argv[2];
const parsedIn = parseInt(firstArg);

if (!isNaN(parsedInt)) {
    console.log(`My number: ${parsedIn}`);
} else {
    console.log("Not a number");
}
