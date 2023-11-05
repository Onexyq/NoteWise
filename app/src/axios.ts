import realAxios from "axios"

const axios = realAxios.create({
    withCredentials: true,
})

export { axios }
