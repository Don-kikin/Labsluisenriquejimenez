// Task 4: delUser(number)import { getServerURL } from './task1.js';
import { getServerURL } from './task1.js'; 

export async function delUser(id) {
  try {
    const url = `${getServerURL()}/users/${id}`;
    await fetch(url, {
      method: 'DELETE'
    });

  } catch (error) {
    console.error("Fallo al eliminar el usuario:", error);
  }
}
