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
		<div class="mx-5 flex-shrink-0 rounded-lg w-24 h-32 bg-col" />
		<div class=" w-9/12 text-2xl lg:text-5xl {e ? 'text-center text-red-500' : 'text-yellow-400'}">
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
		<a href="/">
			<svg
				xmlns="http://www.w3.org/2000/svg"
				width="16"
				height="16"
				fill="currentColor"
				class="telegram rounded-lg p-1 h-8 w-8 text-yellow-400 hover:bg-yellow-400 hover:text-black"
				viewBox="0 0 16 16"
			>
				<path
					fill-rule="evenodd"
					d="m8 3.293 6 6V13.5a1.5 1.5 0 0 1-1.5 1.5h-9A1.5 1.5 0 0 1 2 13.5V9.293l6-6zm5-.793V6l-2-2V2.5a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5z"
				/>
				<path
					fill-rule="evenodd"
					d="M7.293 1.5a1 1 0 0 1 1.414 0l6.647 6.646a.5.5 0 0 1-.708.708L8 2.207 1.354 8.854a.5.5 0 1 1-.708-.708L7.293 1.5z"
				/>
			</svg>
		</a>
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
