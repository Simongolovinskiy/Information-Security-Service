import React from 'react'
import classes from "./Header.module.css"
import asd from "../../images/back.gif"
export default function Header() {
  return (
    <div className={classes.header}>
        <div className="wrapper">
            <div className={classes.headerBody}>
                <div className={classes.title}>Secure data AI</div>
                <ul className={classes.menu}>
                    <li>
                        <a href="#res">Данные</a>
                    </li>
                    <li>
                        <a href="#mail">Почта</a>
                    </li>
                </ul>
                <a className={classes.fireTel} href="tel:1231231123">Горячяя линия 166</a>
            </div>
        </div>
    </div>
  )
}
