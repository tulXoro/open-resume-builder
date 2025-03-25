<script>
	import { onMount } from 'svelte';
	import { ResumeData } from '$lib';

	let userJobTitle = $state('');
	let userJobDesc = $state('');
	let targetJobTitle = $state('');
	let targetJobDesc = $state('');

	let resume = $state('');
	let isLoading = $state(false);
	let selectedModel = $state(''); // Default value
	/**
	 * @type {any[]}
	 */
	let models = $state([]);

	async function getModels() {
		try {
			const response = await fetch('http://localhost:8000/api/models');
			models = await response.json().then((data) => data.models);
			// convert models to array of strings with only name.
			models = models.map((model) => model.name.split(':')[0]);
			selectedModel = models[0];
		} catch (error) {
			console.error(error);
		}
	}

	async function generateResume() {
		isLoading = true;
		try {
			const response = await fetch('http://localhost:8000/api/generate-experience', {
				method: 'POST',
				headers: { 'Content-Type': 'application/json' },
				body: JSON.stringify({
					user_job_title: userJobTitle,
					user_job_description: userJobDesc,
					target_job_title: targetJobTitle,
					target_job_description: targetJobDesc,
					model: selectedModel
				})
			});
			resume = await response.text();
		} catch (error) {
			console.error(error);
			resume = 'Error generating resume';
		}
		isLoading = false;
	}

	onMount(getModels);
</script>

<main>
	<h1>AI Resume Generator</h1>

	<ResumeData />

	<form on:submit|preventDefault={generateResume}>
		<label for="Your Job Title"> Your Job Title </label>
		<input name="Your Job Title" type="text" value={userJobTitle} required />

		<label for="Your Job Description"> What you did: </label>
		<textarea name="Your Job Description" value={userJobDesc} rows="5"></textarea>

		<label for="Target Job Title"> Target Job Title </label>
		<input name="Target Job Title" type="text" value={targetJobTitle} required />

		<label for="Target Job Description"> Job Description </label>
		<textarea name="Target Job Description" value={targetJobDesc} rows="5"></textarea>

		<label>
			AI Model:
			<select>
				{#each models as model}
					<option value={model}>{model}</option>
				{/each}
			</select>
		</label>

		<button type="submit" disabled={isLoading}>
			{isLoading ? 'Generating...' : 'Generate Resume'}
		</button>
	</form>

	{#if isLoading}
		<p>Generating your resume, please wait...</p>
	{/if}

	{#if resume}
		<div class="resume-output">
			<h2>Generated Resume</h2>
			<pre>{resume}</pre>
		</div>
	{/if}
</main>
