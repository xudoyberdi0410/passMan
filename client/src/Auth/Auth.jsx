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
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous"></link>
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