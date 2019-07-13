import React from 'react'
import DetailView from '../component/detailViev'
import axios from 'axios'
import auth_config from '../token'
class GeneralEventDetail extends React.Component {

    state = {
        data : {},
        comments:[]
    }

    fetchComments(){
        const event_id = this.props.match.params.event_id;
        axios.get(`http://127.0.0.1:8000/IMGsched/generalevents/comment/${event_id}`,auth_config).then(
            res => this.setState({comments:res.data})
        )
    }
    fetchDetails(){
        const event_id = this.props.match.params.event_id;
        axios.get(`http://127.0.0.1:8000/IMGsched/generalevents/detail/${event_id}`,auth_config).then(
            res => this.setState({data:res.data})
        )
    }
    componentDidMount(){
        this.fetchComments();
        this.fetchDetails();
    }
    render(){
        return (<DetailView data={this.state.data} comments = {this.state.comments}/>)
    }

}

export default GeneralEventDetail;