import { axios } from "./axios"

export const getMarkDownMindMap = (query: string) => async() =>{
    let r = await axios.post("/api/mindmap", query, {headers: {'Content-Type': 'text/plain'}})
    return r.data
}

export const getExplanation = (query: string) => async() =>{
    let r = await axios.post("/api/explain", query, {headers: {'Content-Type': 'text/plain'}})
    return r.data
}