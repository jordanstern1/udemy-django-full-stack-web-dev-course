var firstName = prompt('What is your first name?')
var lastName = prompt('What is your last name?')
var age = prompt('What is your age?')
var height = prompt('What is your height in cm?')
var petName = prompt("What is your pet's name?")
alert('Thanks for the info!')

cond1 = firstName[0] == lastName[0];
cond2 = age > 20 && age < 30;
cond3 = height >= 170; 
cond4 = petName.slice(-1) === 'y';

if (cond1 && cond2 && cond3 && cond4) {
  console.log("Super secret message!");
} else {
  console.log("Nothing to see.");
}