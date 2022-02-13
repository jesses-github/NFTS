import React, { useEffect, useState } from "react";
// import Header from "./nav-header"
import DisplayWindow from "./Display_Window";
import ScaleLoader from "react-spinners/ScaleLoader"

function App(){
  const [logged_in, logIn] = useState(() => { 
    return false
  })
  // const logged_in = isLoggedIn

  const [loading, setLoading] = useState(false);
  useEffect(() => {
    setLoading(true)
    setTimeout(() => {
      setLoading(false)
    }, 10000)
  }, [])

  function logUserIn() {
    console.log("Logging user in");
    logIn(logged_in => true)
  }

  function logUserOut() {
    console.log("Logging User Out");
    logIn(logged_in => false)
  }

  function toggleLogin() { if (logged_in) { logUserOut() } else { logUserIn() } }

  var loginButton;

  if (logged_in) { loginButton = "Login" } else { loginButton = "Logout"; }

  return ( <div className="app">
    {
      loading ?
      <ScaleLoader height={35} width={35} radius={3} color={"#c282db"} loading={loading} />
    :
      <div>
        <button className="login_button" onClick={toggleLogin}>{loginButton}</button>
        <DisplayWindow />
      </div>
    }
  </div>
  );
}
export default App;