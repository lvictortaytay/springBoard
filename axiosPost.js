//create a get request to the hack or snooze api 

async function getUsers(token){
    const result = await axios.get("https://hack-or-snooze-v3.herokuapp.com/users" , {params: {token}})
    console.log(result)
}


async function signUp(username, password, name){
    const result = await axios.post("https://hack-or-snooze-v3.herokuapp.com/signup" , { user:{name , username, password}})
    console.log(result.data)
}



//login 

async function login(username,password){
    const results = await axios.post("https://hack-or-snooze-v3.herokuapp.com/login" , { user: {username, password}})
    return(results.data.token)
}


async function getUsersWithAuth(){
    const token = await login("lvictortaylor2" , "ednj3233")
    getUsers(token)
}
getUsersWithAuth()
