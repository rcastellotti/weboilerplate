<script>
	import '../app.css';
</script>

<main>
	<slot />
</main>

<style>
	main {
		font-family: 'Electronic Highway Sign' !important;
		flex: 1;
		display: flex;
		flex-direction: column;
		padding: 1rem;
		width: 100%;
		max-width: 1024px;
		margin: 0 auto;
		box-sizing: border-box;
	}
</style>
