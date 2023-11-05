import { Container, Grid } from "@mui/material";
import MarkMapBox from "../components/MarkMapBox";
import useControlStore from "../hooks/useControlStore";
import { useQuery } from "react-query";
import { getMarkDownMindMap } from "../apiFunctions";
import { useEffect } from "react";


const DisplayPage = () => {
    const {index, query} = useControlStore()
    const { data, isLoading, isSuccess, refetch } = useQuery(
        ['get-markdown-mindmap', query], 
        getMarkDownMindMap(query)
    )

    useEffect(()=>{
        if(query !== ""){
            refetch()
        }
    }, [query])

    return (
        <Container maxWidth={false} sx={{ display: "flex", mb:"2rem", alignItems: "center" }}>
            <Grid container sx={{ width: "100%" }}>
                {/* place holder */}
                <Grid item xs={0} md={1} lg={2}></Grid>
                <Grid item xs={12} md={10} lg={8}>
                    {
                        index === 0 ? <MarkMapBox data={data} isLoading={isLoading} /> :
                        <></>
                    }
                </Grid>
                <Grid item xs={0} md={1} lg={2}></Grid>
            </Grid>
        </Container>
    )
}

export default DisplayPage