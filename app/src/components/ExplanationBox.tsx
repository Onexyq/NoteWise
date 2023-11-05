import { LinearProgress, Paper, TextField } from "@mui/material"
import { Box } from "@mui/system"

interface ExplanationBoxProps {
    data: string
    isLoading: boolean
}

const ExplanationBox = (props: ExplanationBoxProps) => {
    const { data, isLoading } = props

    return (
        <Box width="100%">
            <Paper elevation={5}>
                {isLoading && <LinearProgress />}
                <TextField value={data} rows={16} multiline fullWidth />
            </Paper>
        </Box>
    )
}

export default ExplanationBox