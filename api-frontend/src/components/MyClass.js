import React,{Component} from "react";


class MyClass extends Component{
    render(){
        
        return(
            <div>
            <h1>THIS IS A CLASS BASED COMPOPNENT and {this.props.email}..</h1>
            <ul>
                <li>WE HAVE TO IMPORT COMPOPNENT IN BETWWEN CURLY BRACES.</li>
                <li>THEN EXTEND COMPONENT</li>
                <li>RENDER FUNCTION HAS BODY</li>
                <li>INSIDE BODY IT HAS RETURN FUNCTION</li>
                <li>NOW RETURN FUNCTION WILL HAVE 1 ROOT ELEMENT TAG eg:div tag
                <p>AND INSIDE div tag WE CAN PLACE ALL OUR TAGS. </p></li>

            </ul>
            </div>
        )
    }
}

export default MyClass; 