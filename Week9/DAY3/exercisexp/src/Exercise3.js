import React, { Component } from "react";
import './Exercise.css';

class Exercise extends Component {
  render() {
    const styles = {
      heading: {
        color: "red",
        backgroundColor: "lightblue",
        }
    };
      
    const style_header = {
        color: "white",
        backgroundColor: "DodgerBlue",
        padding: "10px",
        fontFamily: "Arial"
    };

    return (
      <div>
        <h1 style={style_header}>This is a Header</h1>
        <p className="para">This is a paragraph</p>
        <a href="#" >
          this is a Link
        </a><br/><br/>
        <form >
          <input type="text" />
          <button type="submit">Submit</button>
            </form><br />
            <h5>Here is an Image:</h5>
            <img src="data:image/png;base64,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" alt="Here is an Image:" />
            <h5>This is a list:</h5>
        <ul >
          <li>Coffee</li>
          <li>Tea</li>
          <li>Milk</li>
        </ul>
      </div>
    );
  }
}

export default Exercise;
