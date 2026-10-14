// const for fixed values
const athleteName = "Brian Otieno";
const protocol = "SMP Phase 1";
const targetSteps = 10000;

// let for values that change
let dayNumber = 1;
let stepCount = 0;

console.log("Athlete:", athleteName);
console.log("Protocol:", protocol);
console.log("Target steps:", targetSteps);

// Reassign let variable
dayNumber = 7;
stepCount = 11240;

console.log("\nDay:", dayNumber);
console.log("Steps logged:", stepCount);
console.log("Hit goal:", stepCount >= targetSteps);

// typeof checks the data type
console.log("\nTypes:");
console.log("athleteName:", typeof athleteName);   // string
console.log("targetSteps:", typeof targetSteps);   // number
console.log("hit goal:",    typeof true);           // boolean
