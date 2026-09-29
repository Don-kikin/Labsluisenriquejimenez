// Task 2: listUsers()
const url = 'http://localhost:3000/users'; 

const listUsers = async () => {
    try {
        const response = await fetch(url);

        if (!response.ok) {
            throw new Error(`Error en la solicitud: ${response.status}`);
        }

        const data = await response.json();
        const formattedUsers = data.map(user => {
            return `{\n  id: ${user.id},\n  first_name: '${user.first_name}',\n  last_name: '${user.last_name}',\n  email: '${user.email}'\n}`;
        });
        
        console.log("[\n" + formattedUsers.join(",\n") + "\n]");
    } catch (error) {
        console.error("Fallo al obtener los usuarios:", error);
    }
};
export { listUsers };