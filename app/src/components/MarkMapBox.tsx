import { Paper } from "@mui/material"
import { Box } from "@mui/system"
import { Transformer } from "markmap-lib"
import { Markmap } from "markmap-view"
import { useEffect, useRef } from "react"


const transformer = new Transformer()

interface MarkMapProps {
    data: string
}

const MarkMapBox = (props: MarkMapProps) => {
    const { data } = props
    const refSvg = useRef<SVGSVGElement>(null)
    const refMm = useRef<Markmap>()

    useEffect(() => {
        if (refSvg.current) {
            const mm = Markmap.create(refSvg.current)
            refMm.current = mm
        }
    }, [])

    useEffect(() => {
        const mm = refMm.current
        if (mm) {
            console.log("hhhhh")
            const { root } = transformer.transform(data);
            mm.setData(root)
            mm.fit()
        }
    }, [refMm.current, data])

    return (
        <Box width="100%">
            <Paper elevation={5}>
                <svg className="mark-map" ref={refSvg} style={{ width: "100%", height: "600px" }} />
            </Paper>
        </Box>
    )
}

export default MarkMapBox