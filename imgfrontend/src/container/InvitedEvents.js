import React from 'react';
import EventList from '../component/GeneralEventList';
import axios from 'axios';
import auth_config from '../token'
import {Icon} from'antd';
import {Link} from 'react-router-dom'
class InvitedEvents extends React.Component {
    state = {
        invitedevents:[]
    }
    fetchInvitedEvents = () =>{
        
        

        axios.get("http://127.0.0.1:8000/IMGsched/invitedevents",auth_config).then(res =>  {
            
        
        this.setState({invitedevents:res.data})})
        
    }
    
    componentDidMount() {
        this.fetchInvitedEvents()
        
    }
    componentWillReceiveProps(newProps) {
        if (newProps.token) {
          this.fetchArticles();      
        }
    }
    render(){
        return(
        <div>
            <EventList data = {this.state.invitedevents}>
            </EventList>
            <Link to = '/invitedevents/add'> <Icon style = {{fontSize:'32px'}} type="plus-circle" /> </Link>
        </div>
        )
    }
};
export default InvitedEvents;
