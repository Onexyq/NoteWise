import { LinearProgress, Paper } from "@mui/material"
import { Box } from "@mui/system"
import { Transformer } from "markmap-lib"
import { Markmap } from "markmap-view"
import { useEffect, useRef } from "react"


const transformer = new Transformer()

interface MarkMapProps {
    data: string
    isLoading: boolean
}

const MarkMapBox = (props: MarkMapProps) => {
    const { data, isLoading } = props
    const refSvg = useRef<SVGSVGElement>(null)
    const refMm = useRef<Markmap>()

    useEffect(() => {
        if (refSvg.current) {
            const mm = Markmap.create(refSvg.current)
            refMm.current = mm
        }
    }, [])


    useEffect(() => {
        if (refMm.current) {
            const { root } = transformer.transform(data ? data : "");
            refMm.current.setData(root)
            refMm.current.fit()
        }
    }, [data])

    return (
        <Box width="100%">
            <Paper elevation={5}>
                {isLoading && <LinearProgress /> }
                <svg className="mark-map" ref={refSvg} style={{ width: "100%", height: "600px" }} />
            </Paper>
        </Box>
    )
}

export default MarkMapBox