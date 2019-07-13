import React from 'react';
import {Descriptions,Comment,List,Form,Input,Button} from 'antd';
const TextArea = Input
const DetailView = props =>(
    <div>
    <Descriptions
        title="Responsive Descriptions"
        border
        column={{ xxl: 4, xl: 3, lg: 3, md: 3, sm: 2, xs: 1 }}
      >
        <Descriptions.Item label='title'>{props.data.title}</Descriptions.Item>
        <Descriptions.Item label="description">{props.data.description}</Descriptions.Item>
        <Descriptions.Item label="Created By">{props.data.createdBy}</Descriptions.Item>
        <Descriptions.Item label="time">{props.data.time}</Descriptions.Item>
        <Descriptions.Item label="Location">{props.data.location}</Descriptions.Item>
        <Descriptions.Item label="Invited Users">{props.data.invitedUsers}</Descriptions.Item>
        
       
      </Descriptions>
      <List className = "Comment"
            dataSource = {props.comments}
            renderItem ={
                (item) => (
                    <li>
                        <Comment 
                        author ={item.user}
                        content={item.content}
                        datetime={item.pub_date}
                        />


                    </li>

                )
            }
            />
        asdsadsa
        <div>
            <Form>
    <Form.Item>
      <TextArea rows={4}  />
    </Form.Item>
    <Form.Item>
      <Button htmlType="submit" type="primary">
        Add Comment
      </Button>
    </Form.Item>
    </Form>
  </div>
    </div>
)

export default DetailView;