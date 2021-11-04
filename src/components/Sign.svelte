<script>
	import { onMount } from 'svelte';
	import { apiUrl } from '$lib/variables';
	import Share from '$components/Share.svelte';
	import { isMobile } from '$lib/stores.js';
	import { goto } from '$app/navigation';
	export let edit, sign, e;
	let message = '';
	let messageInput;
	let response, ctrl;
	let err = '';
	onMount(() => {
		messageInput.focus();
		$isMobile = navigator.userAgentData.mobile; //resolves true/false
	});

	async function saveMessage() {
		await fetch(apiUrl, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({ message: message })
		})
			.then((response) => {
				if (response.ok) {
					return response.json();
				} else {
					throw new Error('Something went wrong');
				}
			})

			.then((res) => {
				response = res;
				setTimeout(() => (response = ''), 2000);
				goto(response.sign.slug);
			})
			.catch((error) => {
				err = error;
				setTimeout(() => (err = ''), 3000);
			});
	}

	function handleKeydown(event) {
		switch (event.keyCode) {
			case 17:
				ctrl = true;
				break;
			case 13:
				if (ctrl) {
					saveMessage();
					ctrl = false;
					return;
				}

			default:
		}
	}
</script>

<svelte:window on:keydown={handleKeydown} />

<div class="p-3 grid grid-cols-1 gap-5 rounded-lg bg-black w-full h-full  border-10 border-col">
	<div class="flex justify-between items-center">
		<div class="ml-5 flex-shrink-0 rounded-lg w-24 h-32 bg-col" />
		<div class="w-9/12 text-2xl lg:text-5xl {e ? 'text-center text-red-500' : 'text-yellow-400'}">
			{#if edit}
				<textarea
					class="resize-none w-full h-full bg-transparent"
					bind:this={messageInput}
					bind:value={message}
					rows="3"
					placeholder="create your custom led message"
				/>
			{:else if e}
				<p class=" w-9/12 text-2xl lg:text-5xl text-red-400">{e}</p>
			{:else}
				{sign}
			{/if}
		</div>
	</div>

	<div class="flex justify-between items-center">
		<p />
		{#if edit}
			{#if response}
				<p class="text1 text-yellow-400">
					successfully created sign <a
						class="hover:bg-yellow-400 hover:text-black p-1 underline"
						href="/{response.sign.slug}">{response.sign.slug}</a
					>
				</p>
			{/if}
			{#if err != ''}
				<p class="text1 text-red-400">an error occurred :(</p>
			{/if}
			<button
				on:click={saveMessage}
				class=" p-1 disabled:opacity-50  rounded-lg bg-green-600 active:bg-green-700  text-white"
				disabled={message.length < 1}
				>save
			</button>
		{:else}
			<Share slug="/" isMobile />
		{/if}
	</div>
</div>
