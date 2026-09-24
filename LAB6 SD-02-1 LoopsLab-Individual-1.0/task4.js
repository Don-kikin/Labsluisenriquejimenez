// Refer to Task 4 in your Instructions to complete this task
let buzzWords = [
    "Fizz",
    "Buzz",
    "FizzBuzz",
    "Woof",
    "Awoo",
    "Bang"
  ];
  
for (let i = 1; i <= 105; i++) {
  let output = "";

  if (i % 3 === 0) {
    output += buzzWords[0];
  } 
  if (i % 5 === 0) { 
    output += buzzWords[1];  
  } 
  if (i % 7 ==0) {
    output += buzzWords[3]
  } 
  if (output === ""){
    console.log(i);
  }else{
    console.log(output);
  }
}
