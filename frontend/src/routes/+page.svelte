<script lang="ts">
	import { onMount } from 'svelte';
	import { ResumeBuilder } from '$lib';

	let userJobTitle = $state('');
	let userJobDesc = $state('');
	let targetJobTitle = $state('');
	let targetJobDesc = $state('');

	let bulletPoints = $state('');
	let isLoading = $state(false);
	let selectedModel = $state(''); // Default value

	let models: any[] = $state([]);

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

	async function generateBulletPoints(event: { preventDefault: () => void; }) {
		event.preventDefault();
		isLoading = true;
    console.log(selectedModel);
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
			bulletPoints = await response.json().then((data) => data.bullet_points);
		} catch (error) {
			console.error(error);
			bulletPoints = 'Error generating bullet points';
		}
		isLoading = false;
	}

	onMount(getModels);
</script>

<h1>AI Resume Generator</h1>

<main class='flex flex-row'>
	

	<ResumeBuilder />
	<form onsubmit={generateBulletPoints}>
		<label for="Your Job Title"> Your Job Title </label>
		<input name="Your Job Title" type="text" bind:value={userJobTitle} required />

		<label for="Your Job Description"> What you did: </label>
		<textarea name="Your Job Description" bind:value={userJobDesc} rows="5"></textarea>

		<label for="Target Job Title"> Target Job Title </label>  
		<input name="Target Job Title" type="text" bind:value={targetJobTitle} required />

		<label for="Target Job Description"> Job Description </label>
		<textarea name="Target Job Description" bind:value={targetJobDesc} rows="5"></textarea>

		<label>
			AI Model:
			<select>
				{#each models as model}
					<option value={model}>{model}</option>
				{/each}
			</select>
		</label>

		<button type="submit" disabled={isLoading}>
			{isLoading ? 'Generating...' : 'Generate Bullet Points'}
		</button>
	</form>

	{#if isLoading}
		<p>Generating your bullet points for {userJobTitle}, please wait...</p>
	{/if}

	{#if bulletPoints}
		<div class="resume-output">
			<h2>Generated Bullet Points</h2>
			<pre>{bulletPoints}</pre>
		</div>
	{/if}
</main>
