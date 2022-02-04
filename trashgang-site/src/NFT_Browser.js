import React from 'react';
import NFTItem from './NFT_Item';
import "./App.css";

function NFTBrowser(){
    let NFTlist = [{key: 1, nft_name:"Random Trash 1", nft_cost: "76", quantity: "5"},
        {key: 2, nft_name: "Get Muscles", nft_cost: "1000", quantity: "1"},
        {key: 3, nft_name: "Space Trash", nft_cost: "1500", quantity: "1"},
        {key: 4, nft_name: "Penis Trash", nft_cost: "15000", quantity: "1"}];
    return (
        <div className="carousel">
            <button className='nav-button'>Scroll Left</button>
            {NFTlist.forEach(function(nft) {console.log(nft)})};
            <>
                {NFTlist.map((nft) => (
                    <NFTItem key={nft.key} nft_name={nft.nft_name} nft_cost={nft.nft_cost} quantity={nft.quantity} />
                ))}
            </>
            {/* {NFTlist.forEach(function(nft) {<NFTItem id = {nft.id} nft_name={nft.nft_name} nft_cost={nft.nft_cost} quantity={nft.quantity } />})}; */}
            {/* <NFTItem nft_name="Random Trash 1" nft_cost="76" quantity="5"/>
            <NFTItem nft_name="Get Muscles" nft_cost="1000" quantity="1"/>
            <NFTItem nft_name="Space Trash" nft_cost="1500" quantity="1"/>
            <NFTItem nft_name="Penis Trash" nft_cost="15000" quantity="1"/> */}
            <button className='nav-button'>Scroll Right</button>
        </div>
    );
}

export default NFTBrowser