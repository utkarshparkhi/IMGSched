import React from 'react';
import { Form, DatePicker, Button,Input } from 'antd';
import axios from 'axios';
import auth_config from '../token'
import {Icon} from'antd';
import {Link} from 'react-router-dom'
class addGeneralEvent extends React.Component {
    
    handleSubmit = e => {
        e.preventDefault();
        
        this.props.form.validateFields((err, values) => {
          if (!err) {
            
           
              
              axios.put('http://127.0.0.1:8000/IMGsched/generalevents',{
                  title:values.title,
                  description:values.description,
                  time:values.time,
                  location:values.location
            },auth_config)
            this.props.history.push('/');
          }
    
          console.log('asdf')
          
          
        });
      };
    
      render() {
        const { getFieldDecorator } = this.props.form;
        
        const config = {
          rules: [{ type: 'object', required: true, message: 'Please select time!' }],
        };
        
        return (
          <div>
          <Form  onSubmit={this.handleSubmit}>
            
            <Form.Item label="Date and time of event">
              {getFieldDecorator('time', config)(
                <DatePicker showTime format="YYYY-MM-DD HH:mm:ss" />,
              )}
            </Form.Item>
           
           
           
           
            <Form.Item>
                {getFieldDecorator('title',{
                    rules :[{
                        
                        required:true,
                        message:'enter the description of your event'}]
                })}
                <Input placeholder ='title'/>
            </Form.Item>
            
            

            <Form.Item>
                {getFieldDecorator('description',{
                    rules :[{

                        required:true,
                        message:'enter the description of your event'}]
                })}
                <Input placeholder ='description'/>
            </Form.Item>


            <Form.Item>
                {getFieldDecorator('location',{
                    rules :[{
                       
                        required:true,
                        message:'enter the location of your event'}]
                })}
                <Input placeholder ='location'/>
            </Form.Item>
            
            
            
            
            
            
            
            
            <Form.Item
              wrapperCol={{
                xs: { span: 24, offset: 0 },
                sm: { span: 16, offset: 8 },
              }}
            >
              <Button type="primary" htmlType="submit">
                Submit
              </Button>
            </Form.Item>
          </Form>
          </div>
        );
      }
}




  


const addGeneralEventForm = Form.create()(addGeneralEvent);
export default addGeneralEventForm;



