import React from "react";
import About from "./About";

export const ComponentBox = ({ content }) => {
    const open = () => {
        console.log("Container opened")
    }
}

return ( 
    <div onClick={open}>
    {content}
    </div>
);

// export default function ContentBox(){
//   return ( <body className="content_box">
//     </body>
//   );
// }
