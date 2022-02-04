import React from "react";
// import Header from "./nav-header"
import DisplayWindow from "./Display_Window";
import trashgangBanner from "./TRASHGANG LUNA Banner.png";

function App(){
  return ( <div className="app">
    {/* <Header /> */}
    <img src={trashgangBanner} alt="Trashgang Banner" className="banner_image"/>
    <DisplayWindow />
    </div>
  );
}
export default App;


      // <button onClick={buyNFT}>Buy NFT</button>
      // <h3>NFTs Owned: {NFTsOwned}</h3> */