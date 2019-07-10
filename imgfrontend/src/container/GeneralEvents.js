import React from 'react';
import GeneralEventList from '../component/GeneralEventList';
import axios from 'axios';
import auth_config from '../token'

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
            <GeneralEventList data = {this.state.generalevents}>
            </GeneralEventList>
        </div>
        )
    }
};
export default GeneralEvents;
