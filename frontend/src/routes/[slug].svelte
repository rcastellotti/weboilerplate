<script context="module">
	import Sign from '$components/Sign.svelte';
	export async function load({ page, fetch }) {
		const res = await fetch('http://backend:5000/' + page.params.slug);
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
	<Sign {sign} />
{/if}
