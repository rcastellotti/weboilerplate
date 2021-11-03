const config = {
	mode: 'jit',
	purge: ['./src/**/*.{html,js,svelte,ts}'],

	theme: {
		backgroundColor: (theme) => ({
			...theme('colors'),
			col: '#161616',
		})
	},

	plugins: []
};

module.exports = config;
