import { Container, Box, Typography, Divider, Button, TextField, Grid } from "@mui/material"
import { Transformer } from 'markmap-lib';
import { Markmap } from 'markmap-view';
import MarkMapBox from "../components/MarkMapBox";
import { useState } from "react";
import useControlStore from "../hooks/useControlStore";





const DisplayPage = () => {
    const [data, setData] = useState("")
    const {index} = useControlStore()
    return (
        <Container maxWidth={false} sx={{ display: "flex", mb:"2rem", alignItems: "center" }}>
            <Grid container sx={{ width: "100%" }}>
                {/* place holder */}
                <Grid item xs={0} md={1} lg={2}></Grid>
                <Grid item xs={12} md={10} lg={8}>
                    {
                        index === 0 ? <MarkMapBox data={data} /> :
                        <></>
                    }
                </Grid>
                <Grid item xs={0} md={1} lg={2}></Grid>
            </Grid>
        </Container>
    )
}

export default DisplayPage