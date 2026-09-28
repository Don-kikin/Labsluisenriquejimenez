export function ageCalculator(year, month, day) {
    const birthYear = Number(year);
    const birthMonth = Number(month) - 1; 
    const birthDay = Number(day);
    const today = new Date();

    let age = today.getFullYear() - birthYear;
    const currentMonth = today.getMonth();
    const currentDay = today.getDate();

    if (currentMonth < birthMonth || (currentMonth === birthMonth && currentDay < birthDay)) {
        age--;
    }
    return age; 
}