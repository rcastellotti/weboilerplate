<script context="module">
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
	function share() {
		if (navigator.share) {
			navigator
				.share({
					title: 'web.dev',
					text: 'Check out web.dev.',
					url: 'https://web.dev/'
				})
				.then(() => console.log('Successful share'))
				.catch((error) => console.log('Error sharing', error));
		}
	}
</script>

<div class="rounded-lg relative h-64 min-h-full bg-col" id="sign">
	<div
		class="relative flex flex-col rounded-lg bg-black inside absolute top-1/2 left-1/2  -translate-x-1/2 -translate-y-1/2"
	>
		<div class="flex m-5">
			<div class="flex-shrink-0 rounded-lg w-24 h-32 bg-col" />
			<div class="flex-shrink-0 rounded-lg ml-2 w-24 h-32 bg-col" />
			<p class=" text1 mx-5 text text-5xl text-yellow-400 ">
				{sign.message}
			</p>
		</div>
		<div class="absolute right-0 bottom-0">
			<a
				href="/{sign.slug}"
				class="p-1 text1 text-xs text-white underline hover:bg-white hover:text-black"
				>signs.rcastellotti.dev/{sign.slug}</a
			>
		</div>
		<div class="flex">
			<svg
				xmlns="http://www.w3.org/2000/svg"
				width="16"
				height="16"
				fill="currentColor"
				class="bi bi-telegram text-yellow-400"
				viewBox="0 0 16 16"
			>
				<path
					d="M13.601 2.326A7.854 7.854 0 0 0 7.994 0C3.627 0 .068 3.558.064 7.926c0 1.399.366 2.76 1.057 3.965L0 16l4.204-1.102a7.933 7.933 0 0 0 3.79.965h.004c4.368 0 7.926-3.558 7.93-7.93A7.898 7.898 0 0 0 13.6 2.326zM7.994 14.521a6.573 6.573 0 0 1-3.356-.92l-.24-.144-2.494.654.666-2.433-.156-.251a6.56 6.56 0 0 1-1.007-3.505c0-3.626 2.957-6.584 6.591-6.584a6.56 6.56 0 0 1 4.66 1.931 6.557 6.557 0 0 1 1.928 4.66c-.004 3.639-2.961 6.592-6.592 6.592zm3.615-4.934c-.197-.099-1.17-.578-1.353-.646-.182-.065-.315-.099-.445.099-.133.197-.513.646-.627.775-.114.133-.232.148-.43.05-.197-.1-.836-.308-1.592-.985-.59-.525-.985-1.175-1.103-1.372-.114-.198-.011-.304.088-.403.087-.088.197-.232.296-.346.1-.114.133-.198.198-.33.065-.134.034-.248-.015-.347-.05-.099-.445-1.076-.612-1.47-.16-.389-.323-.335-.445-.34-.114-.007-.247-.007-.38-.007a.729.729 0 0 0-.529.247c-.182.198-.691.677-.691 1.654 0 .977.71 1.916.81 2.049.098.133 1.394 2.132 3.383 2.992.47.205.84.326 1.129.418.475.152.904.129 1.246.08.38-.058 1.171-.48 1.338-.943.164-.464.164-.86.114-.943-.049-.084-.182-.133-.38-.232z"
				/>
			</svg>
			<a
				href="whatsapp://send?text=%20https://signs.rcastellotti.dev
            "
			>
				<svg
					xmlns="http://www.w3.org/2000/svg"
					width="16"
					height="16"
					fill="currentColor"
					class="w-8 h-8 bi bi-share-fill text-yellow-400"
					viewBox="0 0 16 16"
				>
					<path
						d="M11 2.5a2.5 2.5 0 1 1 .603 1.628l-6.718 3.12a2.499 2.499 0 0 1 0 1.504l6.718 3.12a2.5 2.5 0 1 1-.488.876l-6.718-3.12a2.5 2.5 0 1 1 0-3.256l6.718-3.12A2.5 2.5 0 0 1 11 2.5z"
					/>
				</svg>
			</a>

			<button class="bg-red-900" on:click={share}>asd</button>
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
