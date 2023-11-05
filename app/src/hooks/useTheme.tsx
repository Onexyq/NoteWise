import { createTheme } from "@mui/material";


const useTheme = () => {

    const theme = createTheme();

    theme.typography.h1 = {
        fontSize: '2rem',
        fontWeight: '400',
        '@media (min-width:600px)': {
            fontSize: '4rem',
        },
        [theme.breakpoints.up('md')]: {
            fontSize: '6rem',
        },
    };


    theme.typography.button = {
        ...theme.typography.button,
        [theme.breakpoints.down('md')]: {
            lineHeight: "1",
            fontSize: "0.8rem",
            letterSpacing: "0px"
        },
    };

    theme.palette.primary = {
        ...theme.palette.primary,
        main: "#000"
    }

    return theme
}

export default useTheme