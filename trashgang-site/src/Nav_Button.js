import React from 'react';
import "./App.css";

function NavButton(props){
    return (
        <div className="nav-button">
            <h5>{props.nav_text}</h5>
        </div>
    );
}

export default NavButton