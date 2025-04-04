<script lang="ts">
	import { ResumeData } from "$lib";

</script>

<!-- Resume Container -->
<div class='bg-slate-500 p-12 h-screen overflow-y-scroll w-4xl'>
	<form class='flex flex-col gap-4'>
		<div>
			<h1 class='text-2xl font-bold'>Personal Details</h1>
			<div class='flex flex-col'>
				<label for="full_name"> Full name: </label>
				<input bind:value={ResumeData.fullName} type="text" name="full_name" id="full_name" placeholder="Full name..." required />
			</div>
			
			<div class='flex flex-col'>
				<label for="email"> Email: </label>
				<input bind:value={ResumeData.email} type="email" name="email" id="email" placeholder="Email..." required />
			</div>
			
			<div class='flex flex-col'>
				<label for="phone"> Phone: </label>
				<input bind:value={ResumeData.phone} type="tel" name="phone" id="phone" placeholder="Phone number..." required />
			</div>
		</div>

		<div>

			<div class='flex flex-row'>
				<h1 class='text-2xl font-bold'> Education </h1>

				<button
				class='border-2 border-green-500 bg-green-500 text-white rounded-md p-2 ml-auto mr-0'
				type="button"
				onclick={() => {
					ResumeData.educations = [
						{
							index: ResumeData.educations.length,
							school: '',
							degree: '',
							startDate: '',
							endDate: ''
						},
						...ResumeData.educations 	
					];
				}}
			>
				Add Education
			</button>
			</div>


				{#each ResumeData.educations as form, i}
				<div class='flex flex-col my-4 p-4 border-2 border-gray-300 rounded-md shadow-md'>
					<div class='flex flex-col'>
						<label for="school"> School: </label>
						<input bind:value={form.school} type="text" name="school" id="school" required />
					</div>
					
					<div class='flex flex-col'>
						<label for="degree"> Degree: </label>
						<input bind:value={form.degree} type="text" name="degree" id="degree" required />
					</div>

					<div class='flex flex-col'>
						<label for="start_date"> Start Date: </label>
						<input bind:value={form.startDate} type="date" name="start_date" id="start_date" required />
					</div>

					<div class='flex flex-col'>
						<label for="end_date"> End Date (or expected): </label>
						<input bind:value={form.endDate} type="date" name="end_date" id="end_date" required />
					</div>

					<button
					class='border-2 border-red-500 bg-red-500 text-white rounded-md p-2 ml-auto mr-0 mt-1'
						type="button"
						onclick={() => {
							ResumeData.educations = ResumeData.educations
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

		</div>

	</form>
</div>
