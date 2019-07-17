import React from 'react'
import DetailView from '../component/detailViev'
import axios from 'axios'
import auth_config from '../token'
import {Form,Input,Button} from 'antd'
class InvitedEventDetail extends React.Component {

    state = {
        data : {},
        comments:[],
        newComment:'',
        socket:{},
        token:localStorage.getItem('token')
    }

    fetchComments(){
        const event_id = this.props.match.params.event_id;
        axios.get(`http://127.0.0.1:8000/IMGsched/invitedevent/comments/${event_id}`,auth_config).then(
            res => this.setState({comments:res.data})
        )
    }
    fetchDetails(){
        const event_id = this.props.match.params.event_id;
        axios.get(`http://127.0.0.1:8000/IMGsched/invitedevent/details/${event_id}`,auth_config).then(
            res => 
            {
            var data = res.data;
            var a = data.invitedUsers
            console.log(data)
            a = a.join(' ,')
            data.invitedUsers = a
            this.setState({data:data})
            }
        )
    }
    componentDidMount(){
        this.fetchComments();
        this.fetchDetails();
        const event_id = this.props.match.params.event_id;
        var socket = new WebSocket(`ws://127.0.0.1:8000/IMGsched/invitedevent/${event_id}`    )
        socket.onopen = e => console.log('open',e)
        socket.onmessage = e => {
             console.log('onmessage',e)
             var final_data = this.state.comments.concat(JSON.parse(e.data))

             this.setState({
                 comments:final_data
             })
            }
        this.setState({
            socket:socket
        })
    }
    postComment = (event) => {
        event.preventDefault()
        
        this.state.socket.send(JSON.stringify({
            message:this.state.newComment,
            token:this.state.token
        }))
        this.setState({
            newComment:''
        })
    }
    commentonchange = (event) => {  
        this.setState({
            newComment:event.target.value
        })
    }
    render(){
        return (
            <div>
        <DetailView data={this.state.data} comments = {this.state.comments}/>
            
        
            <Form onSubmit={this.postComment}>
            <Form.Item >
            <Input rows={4} name='comment' onChange={this.commentonchange} value = {this.state.newComment}/>
            </Form.Item>
            <Form.Item>
            <Button htmlType="submit" type="primary">
                Add Comment
            </Button>
            </Form.Item>
            </Form>
        </div>
            )
    }

}

export default InvitedEventDetail;