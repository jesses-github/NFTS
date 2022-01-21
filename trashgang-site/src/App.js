import React, {useState} from "react";
import Header from "./nav-header"
import DisplayWindow from "./Display_Window";
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

function App(){
  return ( <div className="app">
    <Header />
    <DisplayWindow />
    </div>
  );
}
export default App;


      // <button onClick={buyNFT}>Buy NFT</button>
      // <h3>NFTs Owned: {NFTsOwned}</h3> */