<script>
	let education = $state([]);

	let educationForms = $state([]);
</script>

<!-- Resume Container -->
<div>
	<form>
		<label for="full_name"> Full name: </label>
		<input type="text" name="full_name" id="full_name" required />

		<label for="email"> Email: </label>
		<input type="email" name="email" id="email" required />

		<label for="phone"> Phone: </label>
		<input type="tel" name="phone" id="phone" required />

		<span> Education: </span>
		{#each education as edu}
			<div>
				<span>
					School: {edu.school}
				</span>
				<span>
					Degree: {edu.degree}
				</span>
				<span>
					Start Date: {edu.start_date}
				</span>
				<span>
					End Date: {edu.end_date}
				</span>
			</div>
		{/each}
		{#each educationForms as form, i}
			<div>
				<label for="school"> School: </label>
				<input bind:value={form.school} type="text" name="school" id="school" required />
				<label for="degree"> Degree: </label>
				<input bind:value={form.degree} type="text" name="degree" id="degree" required />
				<label for="start_date"> Start Date: </label>
				<input bind:value={form.start_date} type="date" name="start_date" id="start_date" required />
				<label for="end_date"> End Date (or expected): </label>
				<input bind:value={form.end_date} type="date" name="end_date" id="end_date" required />
				<button
					type="button"
					onclick={() => {
						educationForms = educationForms
							.filter((_, index) => index !== i)
							.map((form, newIndex) => ({
								...form,
								index: newIndex
							}));
					}}
				>
					Remove Education
				</button>
			</div>
		{/each}
		<button
			type="button"
			onclick={() => {
				educationForms = [
					...educationForms,
					{
						index: educationForms.length,
						school: '',
						degree: '',
						start_date: '',
						end_date: ''
					}
				];
			}}
		>
			Add Education
		</button>
	</form>
</div>
