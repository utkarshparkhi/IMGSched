import React from 'react';
import { Form,DatePicker,Input ,Button} from 'antd';
import axios from 'axios';
import auth_config from '../token'


class ageForm extends React.Component{

    handleSubmit = (e) =>{
        e.preventDefault()
        const time = e.target.elements.time.value;
        const title = e.target.elements.title.value;
        const location = e.target.elements.location.value;
        const description = e.target.elements.description.value;
        
        
            axios.put('http://127.0.0.1:8000/IMGsched/generalevents',{
                  title:title,
                  description:description,
                  time:time,
                  location:location
            },auth_config);
            this.props.history.push('/');
        }
        
    

    render(){
        return(
            <Form onSubmit = {this.handleSubmit}>

                <Form.Item label= "date of event" required = 'true'>
                    <DatePicker showTime format = "YYYY-MM-DD HH:mm:ss" name='time'/>
                </Form.Item>    
                <Form.Item required = 'true'>
                    <Input name='title' placeholder = 'enter title for your event'/>
                </Form.Item>
                <Form.Item required = 'true'>
                    <Input name='description' placeholder = 'enter description for your event'/>
                </Form.Item>
                <Form.Item required = 'true'>
                    <Input name='location' placeholder = 'enter location for your event'/>
                </Form.Item>
                <Form.Item>
                    <Button htmlType ='submit'>Submit</Button>
                </Form.Item>
            </Form>

        )




    }
}

export default ageForm;