const config = {
	mode: 'jit',
	purge: ['./src/**/*.{html,js,svelte,ts}'],

	theme: {
		backgroundColor: (theme) => ({
			...theme('colors'),
			col: '#161616'
		}),
		borderColor: (theme) => ({
			...theme('colors'),
			col: '#161616'
		}),
		borderWidth: {
			DEFAULT: '1px',
			0: '0',
			2: '2px',
			3: '3px',
			4: '4px',
			6: '6px',
			8: '8px',
			10: '10px'
		}
	},

	plugins: []
};

module.exports = config;
