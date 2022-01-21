import React from 'react';
import NFTItem from './NFT_Item';

function NFTBrowser(){
    return (
        <div className="carousel">
            <button>Scroll Left</button>
            <NFTItem nft_name="Random Trash 1" nft_cost="76" quantity="5"/>
            <NFTItem nft_name="Get Muscles" nft_cost="1000" quantity="1"/>
            <NFTItem nft_name="Space Trash" nft_cost="1500" quantity="1"/>
            <NFTItem nft_name="Penis Trash" nft_cost="15000" quantity="1"/>
            <button>Scroll Right</button>
        </div>
    );
}

export default NFTBrowser