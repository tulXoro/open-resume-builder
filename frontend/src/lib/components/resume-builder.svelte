<script lang="ts">
	import { ResumeData, Education } from '$lib';
</script>

<!-- Resume Container -->
<div class="w-4xl h-screen overflow-y-scroll bg-slate-500 p-12">
	<div class="flex flex-col gap-4">
		<div>
			<h1 class="text-2xl font-bold">Personal Details</h1>
			<div class="flex flex-col">
				<label for="full_name"> Full name: </label>
				<input
					bind:value={ResumeData.fullName}
					type="text"
					name="full_name"
					id="full_name"
					placeholder="Full name..."
					required
				/>
			</div>

			<div class="flex flex-col">
				<label for="email"> Email: </label>
				<input
					bind:value={ResumeData.email}
					type="email"
					name="email"
					id="email"
					placeholder="Email..."
					required
				/>
			</div>

			<div class="flex flex-col">
				<label for="phone"> Phone: </label>
				<input
					bind:value={ResumeData.phone}
					type="tel"
					name="phone"
					id="phone"
					placeholder="(XXX) XXX-XXXX"
					required
				/>
			</div>
		</div>

		<div>
			<div class="flex flex-row">
				<h1 class="text-2xl font-bold">Education</h1>

				<button
					class="ml-auto mr-0 rounded-md border-2 border-green-500 bg-green-500 p-2 text-white"
					type="button"
					onclick={() => {
						ResumeData.educations = [
							{
								// index is only used for the component to know which education it is
								// but we don't need to keep track of it in the array
								index: ResumeData.educations.length,
								school: '',
								degree: '',
								startDate: '',
								endDate: ''
							},
							...ResumeData.educations
						];
						console.log(ResumeData.educations);
					}}
				>
					Add Education
				</button>
			</div>

			<!-- We only need the index of the education because
			 the education component will automatically update itself
			 according to the index it is listed as in the array -->
			{#each ResumeData.educations as _, i}
				<Education 
					{i}
				/>
			{/each}
		</div>



	</div>
</div>
