import React, { useState, useEffect } from 'react';
import "./App.css";
import ScaleLoader from "react-spinners/ScaleLoader"
// import nft from "./Sample NFTs/#6 - L_5-01 Bin_7_Golden_trash-01 with Lid_18_white-01 and Bin_7_Golden_trash-01.jpg"

function NFTItem(props) {
    const [loading, setLoading] = useState(false);
    useEffect(() => {
        setLoading(true)
        return setTimeout(() => {
        setLoading(false)
        }, 10000)
    }, [])
    const setLoad = () => {
        setLoading(false)
    }
        return (
        <div className="nft">
            {
            loading ? 
                <ScaleLoader 
                height={35}
                width={35}
                radius={3}
                color={"#c282db"}
                loading={loading}
                />
            :
            <div>
                <img src={props.nft_url} alt="pic of an nft"></img>
                <h5>{props.nft_key}: {props.nft_name}</h5>
                <p>{props.nft_cost}</p>
                <p>{props.nft_json}</p>
            {/* <p>Limited to: {props.quantity}</p> */}
            </div>
}
        </div>
    );
}

export default NFTItem