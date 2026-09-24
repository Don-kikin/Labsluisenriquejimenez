function Mail(subj, msg) {
    this.subject = subj
    this.message = msg
  }
  
  // Type your code below this line!
  
  const newMail = new Mail("tomato","sauce")
  
  // Type your code above this line!
  
  console.log(newMail.subject + ": " + newMail.message)