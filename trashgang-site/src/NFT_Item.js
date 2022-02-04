import React from 'react';
import "./App.css";
import { useState } from 'react';
// import nft from "./Sample NFTs/#6 - L_5-01 Bin_7_Golden_trash-01 with Lid_18_white-01 and Bin_7_Golden_trash-01.jpg"

function GetLinks(url) {
    var request = new XMLHttpRequest()
    request.open("GET", url, false)
    request.send(null)
    const res_text = request.responseText;
    return JSON.parse(res_text)
}

const json_links = GetLinks("http://127.0.0.1:8000/get_nft_links")
console.log(typeof(json_links))

function NFTItem(props) {
        return (
        <div className="nft">
            <img src={"http://127.0.0.1:8000/random_nft"} alt="pic of an nft"></img>
            <h5>{props.nft_name}</h5>
            <p>${props.nft_cost}</p>
            <p>Limited to: {props.quantity}</p>
        </div>
    );
}

export default NFTItem