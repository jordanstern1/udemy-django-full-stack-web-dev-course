// PART 4 ARRAY EXERCISE
// This is  a .js file with commented hints, its optional to use this.



// Create Empty Student Roster Array
// This has been done for you!
var roster = ['Jose', 'Jordan'];

// Create the functions for the tasks

// ADD A NEW STUDENT

// Create a function called addNew that takes in a name
// and uses .push to add a new student to the array
function addNew(name) {
    roster.push(name);
}

// REMOVE STUDENT

// Create a function called remove that takes in a name
// Finds its index location, then removes that name from the roster

// HINT: http://stackoverflow.com/questions/5767325/how-to-remove-a-particular-element-from-an-array-in-javascript
//
function remove(name) {
    let index = roster.indexOf(name);
    roster.splice(index, 1);
    //alternate solution: roster = roster.filter(x => x != name)
}

// DISPLAY ROSTER

// Create a function called display that prints out the roster to the console.
function display() {
    // alternate solution: roster.forEach(console.log)
    for (name of roster) {
        console.log(name);
    }
}

// Start by asking if they want to use the web app
start = prompt("Would you like to start the roster web app? (y/n)")
should_start = start === 'y'

// Now create a while loop that keeps asking for an action (add,remove, display or quit)
// Use if and else if statements to execute the correct function for each command.
while (should_start) {
    action = prompt('Would you like to add,remove, display, or quit?')
    if (action === 'add') {
        name = prompt('What name would you like to add?')
        addNew(name)
    } else if (action === 'remove') {
        name = prompt('What name would you like to remove?')
        remove(name)
    } else if (action === 'display') {
        display()
    } else if (action === 'quit') {
        should_start = false;
    } else {
        alert('Please select a valid option! Now starting over.')
    }
}

alert("Thanks for using the app! Please refresh to start over.")