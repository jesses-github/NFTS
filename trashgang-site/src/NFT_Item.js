import React from 'react';
import "./App.css";

function NFTItem(props){
    return (
        <div className="nft">
            <h5>{props.nft_name}</h5>
            <p>${props.nft_cost}</p>
            <p>Limited to: {props.quantity}</p>
        </div>
    );
}

export default NFTItem