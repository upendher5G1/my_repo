const prompt=require("prompt-sync")();
let num1 = parseFloat(prompt("Enter first number:"));
let num2 = parseFloat(prompt("Enter second number:"));
let op = prompt("Enter operator (+, -, *, /):");
if (op === "+") {
    console.log("Result:"+(num1+num2));
} else if (op === "-") {
    console.log("Result:"+(num1-num2));
} else if (op === "*") {
    console.log("Result:"+(num1*num2));
} else if (op === "/") {
    if (num2 !== 0) {
        console.log("Result:"+(num1/num2));
    } else {
        console.log("Error: Cannot Divide by Zero");
    }
} else {
    console.log("Invalid operator");
}