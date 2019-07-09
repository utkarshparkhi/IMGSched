import React from 'react';
import { List, Avatar, Popover,Icon } from 'antd';
import {Link} from 'react-router-dom';




const GeneralEventsList =      props =>      (<div><List
    itemLayout="horizontal"
    
    dataSource={props.data}
    renderItem={item => {
      

      const content = (
        <div>
          <p> created by : {item.username} </p>
          <p>description : {item.description}</p>
          <p>location : {item.location}</p>
          <p>time : {item.time}</p>
        </div>
      )
      return (
      
      <List.Item>
        <Popover content = {content} title = {item.title}>
        <List.Item.Meta
          avatar={<Avatar src="https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png" />}
          
          title={<Link to = {`/generalevent/${item.id}`} >{item.title}</Link>}
          description={item.description}
          
        />
        </Popover>
      </List.Item>
     
    )
    }}
    
  />
  <Link to = '/generalevents/add'> <Icon style = {{fontSize:'32px'}} type="plus-circle" /> </Link></div>
  )
  
 


   

export default GeneralEventsList;
  
