const data = {
	login: 'admin',
	password: 'pass123'
}
const send = () => {
    fetch("/req/auth", {
        method: 'POST',
        body: JSON.stringify(data),
    }).then((response) => response.json())
        .then((data) => console.log(data))
        .catch((error) => console.log(error));
};