export function rubricPerfect(score) {
    const numScore = Number(score);

    // Ajustado a la métrica real de tu evaluador (11 es perfecto)
    if (numScore >= 11) { 
        return 'Perfect';
    } else if (numScore >= 9) {
        return 'Excellent';
    } else if (numScore >= 5) { // Asumiendo que 5 sigue siendo la base para aprobar
        return 'Pass';
    } else {
        return 'Fail';
    }
}