<script>
	import { onMount } from 'svelte';
	import { apiUrl } from '$lib/variables';
	import Share from '$components/Share.svelte';
	import { isMobile } from '$lib/stores.js';

	let message = '';
	let messageInput;
	let response,
		err = '';
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
			})
			.catch((error) => {
				err = error;
				setTimeout(() => (err = ''), 3000);
			});
	}
</script>

<div class="rounded-lg relative h-64 min-h-full bg-col" id="message">
	<div
		class=" flex flex-col justify-between rounded-lg bg-black inside absolute top-1/2 left-1/2  -translate-x-1/2 -translate-y-1/2"
	>
		<div class="flex mt-5 mx-5">
			<div class="flex-shrink-0 rounded-lg w-24 h-32 bg-col" />
			<div class="flex-shrink-0 rounded-lg ml-2 w-24 h-32 bg-col hidden lg:block" />
			<p class=" text1 mx-5 text text-2xl lg:text-5xl text-yellow-400 ">
				<textarea
					maxlength="63"
					bind:this={messageInput}
					bind:value={message}
					id="story"
					name="story"
					rows="3"
					cols="21"
					placeholder="create your custom led message"
				/>
			</p>
		</div>
		<div class="m-2 flex justify-between items-end">
			<Share slug="/" isMobile />
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
			<div class="flex items-center flex-col">
				<p
					class="text1 {message.length < 50
						? 'text-green-400'
						: message.length < 60
						? 'text-yellow-400'
						: 'text-red-400'}"
				>
					{message.length}/63
				</p>
				<button
					on:click={saveMessage}
					class="p-1 disabled:opacity-50  rounded-lg bg-green-600 active:bg-green-700  text-white"
					disabled={message.length < 1}
					>save
				</button>
			</div>
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
