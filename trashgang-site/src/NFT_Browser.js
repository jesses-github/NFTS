import React from 'react';
import NFTItem from './NFT_Item';
import "./App.css";

function GetJSON(url) {
    var request = new XMLHttpRequest()
    request.open("GET", url, false)
    request.send(null)
    const res_text = request.responseText;
    return res_text
}

const links_url = "http://127.0.0.1:8000/get_nft_links";
const links_json = JSON.parse(JSON.parse(GetJSON(links_url)));

function GetNFTLink(nft_number) {
    for (var key in links_json[nft_number])
    return links_json[nft_number][key]
}

function GetNFTJSON(nft_number) {
    for (var key in links_json[nft_number]) {
        if (key.split(".")[1] === "json") { return links_json[nft_number][key] }
    }
}

function GetNFTName(nft_number) {
    for (var key in links_json[nft_number])
    return key.split(".")[0]
}

function NFTBrowser(){
    let NFTlist = [];
    let used_keys = [];
    var j = 0;
    for (let i = 1; j < 5; i++) {
        var key = Math.floor(Math.random() * 20);
        if (used_keys.includes(key)) { console.log(`Prevented repeat of ${key}`)} else {
            var nft = {
                "nft_key": key,
                "nft_name": GetNFTName(key),
                "nft_json": GetJSON(GetNFTJSON(i)),
                "nft_url": GetNFTLink(key),
                "nft_cost": "10 Luna"
            }
            used_keys.push(key)
            j = j + 1
            NFTlist.push(nft)
        }
    }
    // let NFTlist = [{key: 1, nft_name:"Random Trash 1", nft_cost: "76", quantity: "5"},
    //     {key: 2, nft_name: "Get Muscles", nft_cost: "1000", quantity: "1"},
    //     {key: 3, nft_name: "Space Trash", nft_cost: "1500", quantity: "1"},
    //     {key: 4, nft_name: "Penis Trash", nft_cost: "15000", quantity: "1"}];
    return (
        <div className='content_box'>
            <h1 className="middle_text_box">Hot Trash!</h1>
            <div className="carousel">
                <div href="ScrollLeft" className="landing_button">Scroll Left</div>
                <>
                    {NFTlist.map((nft) => (
                        <NFTItem className="nft" key={nft["nft_key"]} nft_key={nft["nft_key"]} nft_name={nft["nft_name"]} nft_cost={nft["nft_cost"]} nft_json={nft["nft_json"]} nft_url={nft["nft_url"]}/>
                    ))}
                </>
                <div href="ScrollRight" className="landing_button">Scroll Right</div>
            </div>
        </div>
    );
}

export default NFTBrowser