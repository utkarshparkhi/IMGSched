import React from 'react';
import { Form, Icon, Input, Button, Spin } from 'antd';
import { connect } from 'react-redux';
import { NavLink } from 'react-router-dom';
import * as actions from '../store/actions/auth';
import GoogleLogin from 'react-google-login';
const FormItem = Form.Item;
const antIcon = <Icon type="loading" style={{ fontSize: 24 }} spin />;


class NormalLoginForm extends React.Component {
  handleSubmit = (e) => {
    e.preventDefault();
    this.props.form.validateFields((err, values) => {
      if (!err) {
        this.props.onAuth(values.userName, values.password);
        localStorage.setItem('username',values.userName)
        this.props.history.push('/');
      }
    });
  }

  render() {
    let errorMessage = null;
    if (this.props.error) {
        errorMessage = (
            <p>{this.props.error.message}</p>
        );
    }
    const responseGoogle = (response) => {
        console.log(response);
      }
    const GoogleSuccess = (res) => {
        console.log(res)
        var username = res.w3.U3
        var password = res.w3.Eea
        this.props.onAuth(username,password)
        this.props.history.push('/');
        localStorage.setItem('google_access_token',res.tokenObj.access_token)
    }
    const { getFieldDecorator } = this.props.form;
    return (
        <div>
            <GoogleLogin
    clientId="1009819671620-lcvanu6ml6e5bjftecsjrhi9667alstf.apps.googleusercontent.com"
    buttonText="Login"
    onSuccess={GoogleSuccess}
    onFailure={responseGoogle}
    cookiePolicy={'single_host_origin'}
  />
            {errorMessage}
            {
                this.props.loading ?

                <Spin indicator={antIcon} />

                :

                <Form onSubmit={this.handleSubmit} className="login-form">

                    <FormItem>
                    {getFieldDecorator('userName', {
                        rules: [{ required: true, message: 'Please input your username!' }],
                    })(
                        <Input prefix={<Icon type="user" style={{ color: 'rgba(0,0,0,.25)' }} />} placeholder="Username" />
                    )}
                    </FormItem>

                    <FormItem>
                    {getFieldDecorator('password', {
                        rules: [{ required: true, message: 'Please input your Password!' }],
                    })(
                        <Input prefix={<Icon type="lock" style={{ color: 'rgba(0,0,0,.25)' }} />} type="password" placeholder="Password" />
                    )}
                    </FormItem>

                    <FormItem>
                    <Button type="primary" htmlType="submit" style={{marginRight: '10px'}}>
                        Login
                    </Button>
                    Or 
                    <NavLink 
                        style={{marginRight: '10px'}} 
                        to='/signup/'> signup
                    </NavLink>
                    </FormItem>
                </Form>
            }
      </div>
    );
  }
}

const WrappedNormalLoginForm = Form.create()(NormalLoginForm);

const mapStateToProps = (state) => {
    return {
        loading: state.loading,
        error: state.error
    }
}

const mapDispatchToProps = dispatch => {
    return {
        onAuth: (username, password) => dispatch(actions.authLogin(username, password)) 
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(WrappedNormalLoginForm);