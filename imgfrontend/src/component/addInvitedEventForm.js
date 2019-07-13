import React from 'react';
import { Form,DatePicker,Input ,Button,Checkbox} from 'antd';



const AddInvitedEvent = (props) => (<div>
            <Form onSubmit = {props.handleSubmit} >

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
                <Form.Item required = 'true'>
                    <Checkbox.Group options = {props.data} onChange = {props.onChange} name ='invitedUsers'>
                        
                    </Checkbox.Group>
                </Form.Item>
                
                <Form.Item>
                    <Button htmlType ='submit'>Submit</Button>
                </Form.Item>


            </Form>
            </div>
)

export default AddInvitedEvent;