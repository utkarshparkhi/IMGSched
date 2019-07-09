import React from "react";
import { Route } from "react-router-dom";
import Signup from "./container/Signup"
import GeneralEvents from './container/GeneralEvents'
import InvitedEvents from './container/InvitedEvents'
import Login from "./container/Login";
//import Signup from "./container/Signup";

import ageForm from "./component/addgenereleventform";

const BaseRouter = () => (
  <div>
    <Route exact path='/invitedevents' component = {InvitedEvents} />
    <Route exact path = '/generalevents/add' component = {ageForm} /> 
    <Route exact path='/generalevents/' component ={GeneralEvents} />
    <Route exact path="/signup/" component= {Signup} />
    <Route exact path="/login/" component={Login} />
  </div>
);

export default BaseRouter;