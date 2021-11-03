<script>
	import '../app.css';
	import { onMount } from 'svelte';
	import { isMobile } from '$lib/stores';
	onMount(() => {
		isMobile.set(true);
	});
</script>

<main class=" w-100 m-1 lg:w-2/3 mx-auto">
	<slot />
	<p class="text-sm flex justify-center mt-1 ">
		made with 🛣️,🚘,🚧 by <span class="ml-1"
			><a class="hover:underline" href="https://rcastellotti.dev"> rcastellotti</a></span
		>
	</p>
</main>

<style>
	main {
		font-family: 'Electronic Highway sign' !important;
	}
</style>
