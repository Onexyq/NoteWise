import { axios } from "./axios"

export const getMarkDownMindMap = (query: string) => async() =>{
    let r = await axios.post("/api/data", query, {headers: {'Content-Type': 'text/plain'}})
    return r.data
}