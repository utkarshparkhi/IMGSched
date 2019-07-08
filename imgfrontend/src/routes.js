import React from "react";
import { Route } from "react-router-dom";
import Signup from "./container/Signup"
import GeneralEvents from './container/GeneralEvents'
import Login from "./container/Login";
//import Signup from "./container/Signup";

const BaseRouter = () => (
  <div>
    <Route exact path='/' component ={GeneralEvents} />
    <Route exact path="/signup/" component= {Signup} />
    <Route exact path="/login/" component={Login} />
  </div>
);

export default BaseRouter;