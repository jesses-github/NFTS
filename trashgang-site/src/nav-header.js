import React from 'react';
import AppBar from '@mui/material/AppBar';
import Toolbar from "@mui/material/Toolbar";
import Typography from "@mui/material/Typography";
import Button from "@mui/material/Button";
import IconButton from "@mui/material/IconButton";
import MenuIcon from "@mui/icons-material/Menu"
import { createTheme } from '@mui/material/styles';
import { purple } from '@mui/material/colors';

const theme = createTheme({
  palette: {
    primary: {
      main: purple[500],
    },
    secondary: {
      main: '#f44336',
    },
  },
});

function Header(){
    return (
        <AppBar position="static" color="primary">
            <Toolbar>
                <IconButton size="large" edge="start" color="inherit" aria-label="menu" sx={{ mr: 2 }}>
                    <MenuIcon />
                </IconButton>
                <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
                    Trashgang
                </Typography>
                <Button color="inherit">Login</Button>
            </Toolbar>
        </AppBar>
    );
}
export default Header

        // <div className="header">
        //     <NavButton nav_text="Home"/>
        //     <NavButton nav_text="Get Muscles"/>
        //     <NavButton nav_text="Lore"/>
        //     <NavButton nav_text="Login"/>
        //     <NavButton nav_text="Logout"/>
        // </div>