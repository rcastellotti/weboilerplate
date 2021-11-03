let url;
export const prod = import.meta.env.PROD;

// if (prod) {
// 	url = 'https://signs.rcastellotti.dev/api';
// } else {
	url = 'http://localhost:8000/api';
// }
export const apiUrl = url;
