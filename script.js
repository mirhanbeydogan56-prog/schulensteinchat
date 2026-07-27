import { initializeApp } from "https://www.gstatic.com/firebasejs/10.13.2/firebase-app.js";
import { 
    getDatabase, 
    ref, 
    push, 
    onChildAdded 
} from "https://www.gstatic.com/firebasejs/10.13.2/firebase-database.js";


const firebaseConfig = {
  apiKey: "AIzaSyDGibvGAFm4CSFMvskXmH1weYn1EyDV3yI",
  authDomain: "teett-b2ca0.firebaseapp.com",
  databaseURL: "https://teett-b2ca0-default-rtdb.europe-west1.firebasedatabase.app",
  projectId: "teett-b2ca0",
  storageBucket: "teett-b2ca0.firebasestorage.app",
  messagingSenderId: "409690180731",
  appId: "1:409690180731:web:f9613a3b7626d318cce6de"
};


const app = initializeApp(firebaseConfig);
const db = getDatabase(app);

let user = "";


window.login = function(){

    let password = document.getElementById("pass").value;

    if(password === "mirhan5685"){
        user = "Mirhan";
        document.body.className="mirhan";
    }

    else if(password === "merve5685"){
        user="Merve";
        document.body.className="merve";
    }

    else{
        alert("Yanlış şifre!");
        return;
    }


    document.getElementById("login").style.display="none";
    document.getElementById("chat").style.display="block";

};



window.sendMessage=function(){

    let message=document.getElementById("msg").value;

    if(message.trim()=="") return;


    push(ref(db,"messages"),{
        user:user,
        text:message,
        time:Date.now()
    });


    document.getElementById("msg").value="";
};



onChildAdded(ref(db,"messages"),(data)=>{

    let msg=data.val();

    let box=document.getElementById("messages");


    box.innerHTML += `
    <div class="message">
    <b>${msg.user}</b><br>
    ${msg.text}
    </div>
    `;


    box.scrollTop=box.scrollHeight;

});
