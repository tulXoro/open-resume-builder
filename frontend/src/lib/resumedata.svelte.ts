interface Education {
	index: number;
	school: string;
	degree: string;
	startDate: string;
	endDate: string;
}

interface Experience {
	index: number;
	company: string;
	position: string;
	startDate: string;
	endDate: string;
	bullets: string[];
}

export const ResumeData = $state({
	fullName: '',
	email: '',
	phone: '',
	educations: [] as Education[],
	experiences: [] as Experience[],
	skills: [] as string[]
});
