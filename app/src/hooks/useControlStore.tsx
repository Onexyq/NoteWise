import { create } from 'zustand'

interface useControlStoreProps {
    index: number
    query: string
    setIndex: (index: number) => void
    setQuery: (query: string) => void
}

const useControlStore = create<useControlStoreProps>((set) => ({
    index: -1,
    query: "",
    setIndex: (index: number) => set(() => ({index: index})),
    setQuery: (query: string) => set(() => ({query: query})),
}))

export default useControlStore