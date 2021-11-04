<script context="module">
	// import Share from '$components/Share.svelte';
	import Sign from '$components/Sign.svelte';
	import { apiUrl } from '$lib/variables';
	export async function load({ page, fetch, session, stuff }) {
		const res = await fetch(apiUrl + '/' + page.params.slug);
		if (res.ok) {
			return {
				props: {
					sign: await res.json()
				}
			};
		}

		return {
			props: {
				error: '404 not found'
			}
		};
	}
</script>

<script>
	export let sign, error;
</script>

{#if error}
	<Sign e={error} />
{:else}
	<Sign sign={sign} />
{/if}
