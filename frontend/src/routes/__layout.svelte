<script>
	import '../app.css';
	import { onMount } from 'frontend/node_modules/svelte/types/runtime';
	import { isMobile } from 'frontend/src/lib/stores';
	onMount(() => {
		isMobile.set(true);
	});
</script>

<main class="flex flex-col h-screen justify-between w-100 p-1 lg:w-2/3 mx-auto">
	<div>
		<slot />
	</div>
	<p class="text-sm text-white flex justify-center mt-1 ">
		<a class="text-blue-300 hover:underline" href="https://rcastellotti.dev">source code </a>
		<span class="mx-2"> - </span> made with 🛣️,🚘,🚧 by
		<span class="ml-1">
			<a class=" text-blue-300 hover:underline" href="https://rcastellotti.dev">rcastellotti</a>
		</span>
	</p>
</main>

<style>
	main {
		font-family: 'Electronic Highway sign' !important;
	}
</style>
