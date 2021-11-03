// import { knex } from 'knex';

// knex = knex({
// 	client: 'pg',
// 	connection: {
// 		host: '127.0.0.1',
// 		port: 5432,
// 		user: 'rc',
// 		password: 'ilovebears',
// 		database: 'signs'
// 	}
// });

// export async function post({ params }) {
// 	// const { slug } = params;
// 	// const article = await db.get(slug);
// 	// if (article) {
// 	// 	return {
// 	// 		body: {t
// 	// 			article
// 	// 		}
// 	// 	};
// 	// }
// 	// knex.select().from('signs').timeout(1000);
// }

/**
 * @type {import('@sveltejs/kit').RequestHandler}
 */
export async function get({ params }) {
	// the `slug` parameter is available because this file
	// is called [slug].json.js
	const { slug } = params;

	const article = await db.get(slug);

	if (article) {
		return {
			body: {
				article
			}
		};
	}
}
