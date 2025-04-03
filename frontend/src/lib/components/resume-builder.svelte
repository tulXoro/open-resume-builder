<script lang="ts">

	let educationForms: Education[] = $state([]);

	interface Education {
		index: number;
		school: string;
		degree: string;
		start_date: string;
		end_date: string;
	}



</script>

<!-- Resume Container -->
<div class='bg-teal-500 p-4 h-screen overflow-y-scroll'>
	<form class='flex flex-col gap-4'>
		<div>
			<h1 class='text-2xl font-bold'>Personal Details</h1>
			<div>
				<label for="full_name"> Full name: </label>
				<input type="text" name="full_name" id="full_name" required />
			</div>
			
			<div>
				<label for="email"> Email: </label>
				<input type="email" name="email" id="email" required />
			</div>
			
			<div>
				<label for="phone"> Phone: </label>
				<input type="tel" name="phone" id="phone" required />
			</div>
		</div>

		<div>
			<h1 class='text-2xl font-bold'> Education: </h1>

				{#each educationForms as form, i}
				<div class='my-4 p-4 border-2 border-gray-300 rounded-md'>
					<div>
						<label for="school"> School: </label>
						<input bind:value={form.school} type="text" name="school" id="school" required />
					</div>
					
					<div>
						<label for="degree"> Degree: </label>
						<input bind:value={form.degree} type="text" name="degree" id="degree" required />
					</div>

					<div>
						<label for="start_date"> Start Date: </label>
						<input bind:value={form.start_date} type="date" name="start_date" id="start_date" required />
					</div>

					<div>
						<label for="end_date"> End Date (or expected): </label>
						<input bind:value={form.end_date} type="date" name="end_date" id="end_date" required />
					</div>

					<button
					class='border-2 border-red-500 bg-red-500 text-white rounded-md p-2'
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
				class='border-2 border-green-500 bg-green-500 text-white rounded-md p-2'
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
		</div>

	</form>
</div>
