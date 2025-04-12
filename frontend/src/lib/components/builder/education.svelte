<script>
  import { ResumeData } from '$lib';

  let {
    i
  } = $props();
</script>


<div class="my-4 flex flex-col rounded-md border-2 border-gray-300 p-4 shadow-md">
  <div class="flex flex-col">
    <label for="school"> School: </label>
    <input bind:value={ResumeData.educations[i].school} type="text" name="school" id="school" required />
  </div>

  <div class="flex flex-col">
    <label for="degree"> Degree: </label>
    <input bind:value={ResumeData.educations[i].degree} type="text" name="degree" id="degree" required />
  </div>

  <div class="flex flex-col">
    <label for="start_date"> Start Date: </label>
    <input
      bind:value={ResumeData.educations[i].startDate}
      type="date"
      name="start_date"
      id="start_date"
      required
    />
  </div>

  <div class="flex flex-col">
    <label for="end_date"> End Date (or expected): </label>
    <input bind:value={ResumeData.educations[i].endDate} type="date" name="end_date" id="end_date" required />
  </div>

  <button
    class="ml-auto mr-0 mt-1 rounded-md border-2 border-red-500 bg-red-500 p-2 text-white"
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