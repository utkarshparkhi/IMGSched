import React from "react";
import { Route } from "react-router-dom";
import Signup from "./container/Signup"
import GeneralEvents from './container/GeneralEvents'
import InvitedEvents from './container/InvitedEvents'
import Login from "./container/Login";
import AieForm from "./container/aieForm";
import GeneralEventDetail from './container/GeneralEventDetail'
//import Signup from "./container/Signup";
import InvitedEventDetail from './container/InvitedEventDetails'
import ageForm from "./component/addgenereleventform";

const BaseRouter = () => (
  <div> 
    <Route exact path='/invitedevent/:event_id' component = {InvitedEventDetail}/>
    <Route exact path='/generalevent/:event_id'component ={GeneralEventDetail} />
    <Route exact path='/invitedevents/add' component = {AieForm} />
    <Route exact path='/invitedevents' component = {InvitedEvents} />
    <Route exact path = '/generalevents/add' component = {ageForm} /> 
    <Route exact path='/generalevents/' component ={GeneralEvents} />
    <Route exact path="/signup/" component= {Signup} />
    <Route exact path="/login/" component={Login} />
  </div>
);

export default BaseRouter;