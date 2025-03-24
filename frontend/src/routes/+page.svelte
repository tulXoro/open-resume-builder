<script>
  let background = '';
  let jobDescription = '';
  let resume = '';
  let isLoading = false;
  let selectedModel = 'mixtral'; // Default value
  const MODELS = [
    { name: 'Mixtral (Best)', value: 'mixtral' },
    { name: 'Llama3 (Fast)', value: 'llama3' },
    { name: 'Phi-3 (Lightweight)', value: 'phi3' },
    { name: 'Llama2 (Balanced)', value: 'llama2' },
  ];

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
</script>

<main>
  <h1>AI Resume Generator</h1>
  <form on:submit|preventDefault={generateResume}>
    <label>
      Your Background:
      a
      <textarea bind:value={background} rows="5"></textarea>
    </label>
    
    <label>
      Job Description:
      <textarea bind:value={jobDescription} rows="5"></textarea>
    </label>
    
    <label>
      AI Model:
      <select bind:value={selectedModel}>
        {#each MODELS as model}
          <option value={model.value}>{model.name}</option>
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