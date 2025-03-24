<script>
	import { onMount } from "svelte";

  let background = $state('');
  let jobDescription = $state('');
  let resume = $state('');
  let isLoading = $state(false);
  let selectedModel = $state(''); // Default value
  /**
	 * @type {any[]}
	 */
  let models = $state([]);

  async function getModels () {
    try {
      const response = await fetch('http://localhost:8000/api/models');
      models = await response.json().then(data => data.models);
      // convert models to array of strings with only name.
      models = models.map(model => model.name.split(':')[0]);
      selectedModel = models[0];
    } catch (error) {
      console.error(error);
    }
  }

  async function generateResume() {
    isLoading = true;
    try {
      const response = await fetch('http://localhost:8000/api/generate-resume', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ 
          background: background,
          job_description: jobDescription,
          model: selectedModel
         })
      });
      resume = await response.text();
    } catch (error) {
      console.error(error);
      resume = "Error generating resume";
    }
    isLoading = false;
  }

  onMount(getModels);

</script>

<main>
  <h1>AI Resume Generator</h1>
  <form on:submit|preventDefault={generateResume}>
    <label>
      Your Background:
      a
      <textarea value={background} rows="5"></textarea>
    </label>
    
    <label>
      Job Description:
      <textarea value={jobDescription} rows="5"></textarea>
    </label>
    
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