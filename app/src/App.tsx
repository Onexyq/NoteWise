
import { Box, Container, TextField, ThemeProvider, createTheme } from "@mui/material"
import TextEntryPage from "./pages/TextEntryPage"
import StartPage from "./pages/StartPage"
import DisplayPage from "./pages/DisplayPage"
import { QueryClient, QueryClientProvider } from "react-query"
import useTheme from "./hooks/useTheme"

const queryClient = new QueryClient({
    defaultOptions: {
        queries: {
            refetchOnWindowFocus: false,
            staleTime: 60 * 1000, // 1 minute
        },
    },
})

const App = () => {
    const theme = useTheme()
    return (
        <ThemeProvider theme={theme}>
            <QueryClientProvider client={queryClient}>
                <StartPage />
                <TextEntryPage />
                <DisplayPage />
            </QueryClientProvider>
        </ThemeProvider>
    )
}

export default App