import React from 'react';
import { List, Avatar, Popover } from 'antd';
import {Link} from 'react-router-dom';



const EventsList =      props =>      (<div><List
    itemLayout="horizontal"
    
    dataSource={props.data}
    renderItem={item => {
      

      const content = (
        <div>
          <p> created by : {item.username} </p>
          <p>description : {item.description}</p>
          <p>location : {item.location}</p>
          <p>time : {item.time}</p>
          <p>invited users: {item.invitedUsers.join(', ')}</p>
        </div>
      )
      return (
        
      <List.Item>
        <Link to = {`${item.name}/${item.id}`}>
        <Popover content = {content} title = {item.title}>
       
        <List.Item.Meta
          avatar={<Avatar src="https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png" />}
          
          title= {item.title}
          description={item.description}
          
        />
         
        </Popover>
        </Link>
      </List.Item>
     
     
    )
    }}
    
  />
  
  
  
  
  </div>
  )
  
 


   

export default EventsList;
  
