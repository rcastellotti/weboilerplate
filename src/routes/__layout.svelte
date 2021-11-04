<script>
	import '../app.css';
	import { onMount } from 'svelte';
	import { isMobile } from '$lib/stores';
	onMount(() => {
		isMobile.set(true);
	});
</script>

<main class="flex flex-col h-screen justify-between w-100 p-1 lg:w-2/3 mx-auto">
	<div>
		<slot />
	</div>
	<p class="text-sm flex justify-center mt-1 ">
		<a class="hover:bg-blue-300 text-blue-700 hover:underline" href="https://rcastellotti.dev">source code </a> 
		<span class="mx-2"> - </span> made with
		🛣️,🚘,🚧 by
		<span class="ml-1"
			><a class="hover:bg-blue-300 text-blue-700 hover:underline" href="https://rcastellotti.dev">
				rcastellotti</a
			></span
		>
	</p>
</main>

<style>
	main {
		font-family: 'Electronic Highway sign' !important;
	}
</style>
