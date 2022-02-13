import React from "react";
import NFTBrowser from "./NFT_Browser";
import About from "./About";
import LandingSplash from "./LandingSplash";

export default function DisplayWindow(){
  return ( <div className="content_box">
    <LandingSplash />
    <About />
    <NFTBrowser />
    </div>
  );
}