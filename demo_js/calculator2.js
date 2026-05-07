function calculator(){
    const prompt=require("prompt-sync")();
    while(true){
        console.log("....Simple Calculator....");
        console.log("Enter 'x' For Exit Calculator")
        let a = parseFloat(prompt("Enter first number:"));
        let b = parseFloat(prompt("Enter second number:"));
    let op = prompt("Enter operator (+, -, *, /):");
    if (op==='x'){
        console.log("Calculator Closed...")
        break;
    }
    switch (op) {
        case '+':
            console.log("Result:"+(a+b));
            break;
        case '-':
            console.log("Result:"+(a-b));
            break;
        case '*':
            console.log("Result:"+(a*b));
            break;
        case '/':
            if (b != 0)
                console.log("Result: " + (a / b));
                else
                    console.log("Error:Cannot Divide By Zero");
            break;
        default:
            console.log("invalid choice");
        break;
        }
    }
}
calculator();