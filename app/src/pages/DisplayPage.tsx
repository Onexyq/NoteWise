import { Container, Box, Typography, Divider, Button, TextField } from "@mui/material"






const DisplayPage = () => {
    return (
        <Box display="flex" flexDirection="column" gap="2rem" justifyContent="center" alignItems="center" >
            <TextField multiline rows={16} sx={{mt: "2rem", mb: "10rem", width:"80%"}}/>
        </Box>
    )
}

export default DisplayPage