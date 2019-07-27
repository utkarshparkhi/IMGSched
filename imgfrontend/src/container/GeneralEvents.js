import React from 'react';
import EventList from '../component/GeneralEventList';
import axios from 'axios';
import auth_config from '../token'
import {Icon} from'antd';
import {Link} from 'react-router-dom'
class GeneralEvents extends React.Component {
    state = {
        generalevents:[]
    }
    fetchGeneralEvents = () =>{
        
        

        axios.get("http://127.0.0.1:8000/IMGsched/generalevents",auth_config).then(res =>  
        {
        
        this.setState({generalevents:res.data})})
        
    }
    
    componentDidMount() {
        this.fetchGeneralEvents()
        
    }
    componentWillReceiveProps(newProps) {
        if (newProps.token) {
          this.fetchArticles();      
        }
    }
    render(){
        return(
        <div>
            <EventList data = {this.state.generalevents}>
            </EventList>

          <Link to = '/generalevents/add'> <Icon style = {{fontSize:'32px'}} type="plus-circle" /> </Link>
        </div>
        )
    }
};
export default GeneralEvents;
