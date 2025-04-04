interface Education {
    index: number
    school: string
    degree: string
    startDate: string
    endDate: string
}

export const ResumeData=$state({
    fullName:"",
    email:"",
    phone:"",
    educations: [] as Education[],
})