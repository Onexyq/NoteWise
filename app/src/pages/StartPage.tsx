import { Box, Button, Container, Divider, Typography } from "@mui/material"
import animateScrollTo from 'animated-scroll-to';




const StartPage = () => {
    const ScrollToTextEntryPage = () => {
        let element = document.getElementById("text-entry-page")!
        animateScrollTo(element, { speed: 1000 })
    }

    return (
        <Container maxWidth={false} sx={{ height: "100vh", display: "flex", flexDirection: "column", gap: "2rem", justifyContent: "center", alignItems: "center" }}>
            <Typography variant="h1">Welcome to <b>NoteWise</b></Typography>
            <Divider sx={{ width: "72%", borderWidth: "2px", background: "#000", marginBottom: "4rem" }} />
            <Button variant="outlined" size="large" onClick={ScrollToTextEntryPage}>Get Started</Button>
        </Container>
    )
}

export default StartPage