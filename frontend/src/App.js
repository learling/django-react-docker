
import logo from "./logo.svg";
import "./App.css";
import axios from "axios";
import React from "react";

const baseURL = "http://127.0.0.1:8765/api/";

function App() {
  const [data, setData] = React.useState({message: ""});

  React.useEffect(() => {
    axios.get(baseURL).then((response) => {
      console.log(response);
      setData(response.data);
    });
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>{data.message}</p>
      </header>
    </div>
  );
}

export default App;
