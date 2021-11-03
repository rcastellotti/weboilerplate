<script context="module">
	// import Share from '$components/Share.svelte';
	import Sign from '$components/Sign.svelte';
	import { apiUrl } from '$lib/variables';
	export async function load({ page, fetch, session, stuff }) {
		if (page.params.slug == 'bootstrap.min.css.map') return;
		const res = await fetch(apiUrl + '/' + page.params.slug);
		if (res.ok) {
			return {
				props: {
					sign: await res.json()
				}
			};
		}

		return {
			status: res.status,
			error: new Error(`Could not load`)
		};
	}
</script>

<script>
	export let sign;
</script>

<Sign sign={sign.message} />
