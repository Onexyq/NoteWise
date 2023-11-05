import { create } from 'zustand'

interface useControlStoreProps {
    index: number
    setIndex: (index: number) => void
}

const useControlStore = create<useControlStoreProps>((set) => ({
    index: -1,
    setIndex: (index: number) => set(() => ({index: index}))
}))

export default useControlStore