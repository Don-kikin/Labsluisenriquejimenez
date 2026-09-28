export function rubricPassFail(score) {
    if (score >= 5) { // Usa el número de aprobación que te hayan dado
        return 'Pass'; // <-- Usa RETURN, no console.log
    } else {
        return 'Fail';
    }
}