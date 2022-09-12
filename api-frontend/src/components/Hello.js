import React from "react";


// function Hellso() {
//     return(
//         <h1>WE ARE INSIDE THE FUNCTION</h1>
//     )
// }

// export default Hello;


function FuncComponent(params) {

    function ClickMe(params) {
        alert("Button is clicked")
    }

    return(
        // <h1>WE ARE INSIDE THE FUNCTION</h1>
        
        <div>
            <h1>Hello im trying the name property in this headder {params.name}</h1>
        <button onClick={ClickMe}>Click Me</button>
        </div>
    )
}

export default FuncComponent;