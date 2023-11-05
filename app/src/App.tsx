
import { Box, Container, TextField } from "@mui/material"
import TextEntryPage from "./pages/TextEntryPage"
import StartPage from "./pages/StartPage"
import DisplayPage from "./pages/DisplayPage"
import { QueryClient, QueryClientProvider } from "react-query"

const queryClient = new QueryClient({
    defaultOptions: {
        queries: {
            refetchOnWindowFocus: false,
            staleTime: 60 * 1000, // 1 minute
        },
    },
})

const App = () => {
    return (
        <QueryClientProvider client={queryClient}>
            <StartPage/>
            <TextEntryPage/>
            <DisplayPage/>
        </QueryClientProvider>
    )
}

export default App