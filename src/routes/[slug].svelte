<script context="module">
    import Share from '$components/Share.svelte';
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

<div class="rounded-lg relative h-64 min-h-full bg-col" id="sign">
	<div
		class="flex flex-col justify-between rounded-lg bg-black inside absolute top-1/2 left-1/2  -translate-x-1/2 -translate-y-1/2"
	>
		<div class="flex m-5">
			<div class="flex-shrink-0 rounded-lg w-24 h-32 bg-col" />
			<div class="flex-shrink-0 rounded-lg ml-2 w-24 h-32 bg-col" />
			<p class=" text1 mx-5 text text-5xl text-yellow-400 ">
				{sign.message}
			</p>
		</div>

		<div class="flex justify-end m-1">
			<Share slug={`/${sign.slug}`} navigator />
		</div>
	</div>
</div>

<style>
	.inside {
		height: 15rem;
		width: 98%;
		height: 95%;
	}
	textarea {
		background-color: transparent !important;
	}
</style>
