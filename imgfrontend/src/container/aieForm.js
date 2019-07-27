import React from 'react';
import AddInvitedEvent from '../component/addInvitedEventForm';
import axios from 'axios'
import auth_config from '../token'

class AieForm extends React.Component{
    state = {
        users:[],
        invitedUsers:[]
    };


    componentDidMount= () =>{
        axios.get('http://127.0.01:8000/authentication/getall',auth_config)
        .then(res => {this.setState({users:res.data})})
    }

  handleSubmit = (e) =>{
        e.preventDefault()
        const time = e.target.elements.time.value;
        const title = e.target.elements.title.value;
        const location = e.target.elements.location.value;
        const description = e.target.elements.description.value;
        const invited_users = this.state.invitedUsers
        console.log(title)
        console.log(invited_users)
        
            axios.put('http://127.0.0.1:8000/IMGsched/invitedevents',{
                  title:title,
                  description:description,
                  time:time,
                  location:location,
                  invitedUsers:invited_users
            },auth_config);
            this.props.history.push('/');
        }

     onChange = (checkedValues) => {
         this.setState({invitedUsers:checkedValues})
        
         console.log(checkedValues)
    }

    
    render(){
        


        return(<div>           <AddInvitedEvent data = {this.state.users} handleSubmit = {this.handleSubmit} onChange = {this.onChange}/>
 
 
        </div>
 
        )
    }


}

export default AieForm;
