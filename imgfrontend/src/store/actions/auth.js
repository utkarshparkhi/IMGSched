import * as actionTypes from './actionTypes'
import axios from 'axios';

export const authStart = () => {
    return ({
        type:actionTypes.AUTH_START
    })
};

export const authSuccess = token => {
    return ({
        type:actionTypes.AUTH_SUCCESS,
        token: token
    })
};


export const authFail = error => {
    return ({
        type:actionTypes.AUTH_FAIL,
        error: error
    })
};

export const logout = () => {
    axios.post('http://127.0.0.1:8000/authentication/token/revoke/',{
        token:localStorage.getItem('token')
    });
    localStorage.removeItem('token');
    localStorage.removeItem('expiresIn');
    return {
        type:actionTypes.AUTH_LOGOUT
    }
};

export const checkAuthTimeout = expiresIn => {
    return dispatch => {
        setTimeout(() => {
            dispatch(logout())
        }, expiresIn*1000);
    }
};

export const authLogin = (username,password) => {
    return dispatch =>{
        dispatch(authStart());
        axios.post('http://127.0.0.1:8000/authentication/token/',{
            username:username,
            password:password,
        }).then(res => {
            const token = res.data.access_token
            const expiresIn = res.data.expires_in
            localStorage.setItem('token',token);
            localStorage.setItem('expiresIn',expiresIn);
            dispatch(authSuccess(token));
            
        })
        .catch(err => {
            dispatch(authFail(err))
        })

    }
};

export const authSignup = (username,email,password,first_name,last_name) => {
    return dispatch =>{
        dispatch(authStart());
        axios.post('http://127.0.0.1:8000/authentication/register/',{
            username:username,
            password:password,
            email:email,
            first_name:first_name,
            last_name:last_name
        }).then(res => {
            const token = res.data.access_token
            const expiresIn = res.data.expires_in
            localStorage.setItem('token',token);
            localStorage.setItem('expiresIn',expiresIn);
            dispatch(authSuccess(token));
            
        })
        .catch(err => {
            dispatch(authFail(err))
        })

    }
}


export const authCheckState = () => {
    return dispatch => {
        const token = localStorage.getItem('token');
        if(token === undefined) {
            dispatch(logout());
        }
        
    }
}