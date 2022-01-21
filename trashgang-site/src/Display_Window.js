import React, {useState} from "react";
import NFTBrowser from "./NFT_Browser";
import About from "./About";

export default function DisplayWindow(){
  return ( <div className="display_window">
    <About />
    <h1 className="about">Hot Trash!</h1>
    <NFTBrowser />
    </div>
  );
}