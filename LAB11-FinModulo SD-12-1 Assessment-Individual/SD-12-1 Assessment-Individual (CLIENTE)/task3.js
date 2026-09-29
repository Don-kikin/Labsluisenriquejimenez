// Task 3: addUser(first_name, last_name, email)
import { getServerURL } from './task1.js';

export async function addUser(first_name, last_name, email) {
  try {
    const url = `${getServerURL()}/users`;
    const response = await fetch(url);
    const users = await response.json();

    let maxId = 0;
    for (let i = 0; i < users.length; i++) {
      const currentId = Number(users[i].id); 
      if (currentId > maxId) {
        maxId = currentId;
      }
    }

    const newUser = {
      id: maxId + 1,
      first_name: first_name,
      last_name: last_name,
      email: email
    };

    await fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(newUser)
    });

    const formattedUser = `{\n  id: ${newUser.id},\n  first_name: '${newUser.first_name}',\n  last_name: '${newUser.last_name}',\n  email: '${newUser.email}'\n}`;
    console.log(formattedUser);

  } catch (error) {
    console.error("Fallo al agregar el usuario:", error);
  }
}