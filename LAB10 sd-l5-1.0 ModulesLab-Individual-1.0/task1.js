export function costCalculator(amount) {
    const costNum = Number(amount);
    const fee = 3;
    return costNum + fee + interes(costNum);
}

export function interes(amount) {
    return amount * 0.01;
}