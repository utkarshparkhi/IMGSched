const token = localStorage.getItem('token')
const auth_config = {
            headers: {'Authorization':"Bearer "+ token}
        }
export default auth_config;