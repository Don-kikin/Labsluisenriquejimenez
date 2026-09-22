// Refer to Task 2 in your Instructions to complete this task

let buzzWords = [
    "Fizz",
    "Buzz",
    "FizzBuzz",
    "Bark",
    "Awoo",
    "Bang"
];
  
for (let i = 1; i <= 105; i++) {
  if (i % 3 === 0) {
    console.log(buzzWords[0]);  
  } else {
    console.log(i);
  }
}