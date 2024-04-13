import React, { useState } from 'react'
import classes from "./Hero.module.css"
import heroImage from "../../images/hero.svg"
export default function Hero() {

  const [emailText, setEmailText] = useState("") 
  const [err, setErr] = useState(true)
  const mailRegex = (value) => {
    setEmailText(value)
    const regex = /^(([^<>()[\]\.,;:\s@\"]+(\.[^<>()[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i
    if(value === ""){
        setErr(true)
        return
    }
    if(value.replace(regex, "") === ""){
        setErr(false)
    }
    else{
        setErr(true)
    }
  }

  const submitEmail = () => {
    console.log(emailText)
  }

  return (
    <div className='wrapper'>
        <div className={classes.heroBody}>
            <div id='mail' className={classes.heroTextBox}>
                <h1>Все показатели трафика <br/> у вас на ладони</h1>
                <p>Система проверки на основе решений ИИ</p>
                <div className={classes.form}>
                    <input onChange={(e) => mailRegex(e.target.value)} type="text" placeholder='Ваш имейл'/>
                    <button disabled={err} onClick={submitEmail} className={classes.btn}>На эту почту</button>
                </div>
            </div>
            <div className={classes.imageBox}>
                <img src={heroImage} alt="" />
            </div>
        </div>
    </div>
  )
}
