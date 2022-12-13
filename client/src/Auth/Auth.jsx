import axios from "axios"
import { useState } from "react";

const Auth = () => {
    const [form, setForm] = useState({
        username: '',
        password: '',
    })
    const formHandler = (event) => {
        setForm({...form, [event.target.name]: event.target.value})
    }
    const reg = () => {
        axios.post('/reg', form).then(res => console.log(res.data))
    }
    const log = () => {
        axios.post('/log', form).then(res => console.log(res.data))
    }
    return ( 
        <main>
            <div>
                <input type="text" name="username" placeholder="Username" onChange={formHandler}/>
                <input type="password" name="password" placeholder="Password" onChange={formHandler}/>
                <button type="submit" onClick={reg}>Join In</button>
                <button type="submit" onClick={log}>Sign In</button>
            </div>
        </main>
     );
}
 
export default Auth;