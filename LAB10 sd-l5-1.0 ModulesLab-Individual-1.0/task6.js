export function rubricExcellent(score) {
    const numScore = Number(score);

    if (numScore >= 9) {
        return 'Excellent';
    } 

    else if (numScore >= 5) { 
        return 'Pass';
    } 

    else {
        return 'Fail';
    }
}