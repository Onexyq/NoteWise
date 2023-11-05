import { Box, Button, Container, Grid, TextField, Typography } from "@mui/material"
import { AccountTree, CoPresent, Description } from '@mui/icons-material';
import { useEffect, useRef, useState } from "react";
import animateScrollTo from "animated-scroll-to";


const BUTTON_GROUPS = [
    { name: "MindMap", icon: <AccountTree /> },
    { name: "PPT Slides", icon: <CoPresent /> },
    { name: "Notes", icon: <Description /> }
]


const TextEntryPage = () => {
    const [checked, setChecked] = useState(-1)
    const buttonGroupRef = useRef<Element>()

    const onScroll = () =>{
        if (buttonGroupRef.current) {
            let element = buttonGroupRef.current
            let elemRect = element.getBoundingClientRect()
            if (elemRect.top < 30 && !element.classList.contains("Down")){
                element.classList.remove("Up")
                element.classList.add("Down")
            }
            
            if (elemRect.bottom > 300 && !element.classList.contains("Up")){
                element.classList.remove("Down")
                element.classList.add("Up")
            }
        }
    }

    useEffect(() => {
        window.addEventListener("scroll", onScroll, {passive: false})
      return () => {
        window.removeEventListener("scroll", onScroll)
      }
    }, [])
    

    const ClickButton = (index: number) =>{
        setChecked(index)
        if (buttonGroupRef.current) {
            animateScrollTo(buttonGroupRef.current, { speed: 1000 })
        }
    }

    return (
        <Container id="text-entry-page" maxWidth={false} sx={{ mt: "4rem", height:"100vh", display:"flex", alignItems:"center" }}>
            <Grid container sx={{ width: "100%"}}>
                {/* place holder */}
                <Grid item xs={0} md={1} lg={2}></Grid>
                <Grid item xs={12} md={10} lg={8}>
                    <Typography fontWeight={600} sx={{m: "1rem"}}>Put Your Drafts Here:</Typography>
                    <TextField multiline fullWidth rows={16}/>
                    <Box ref={buttonGroupRef} display="flex" justifyContent="space-around" marginTop="2rem">
                        {
                            BUTTON_GROUPS.map((button, index) => (
                                <Button
                                    variant={checked === index ? "contained" : "outlined"}
                                    size="large"
                                    startIcon={button.icon}
                                    key={button.name}
                                    onClick={()=>ClickButton(index)}
                                >
                                    {button.name}
                                </Button>
                            ))
                        }
                    </Box>
                </Grid>
                {/* place holder */}
                <Grid item xs={0} md={1} lg={2}></Grid>
            </Grid>
        </Container>
    )
}

export default TextEntryPage