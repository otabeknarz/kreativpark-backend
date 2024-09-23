import './Header.css'
// import Button from "../base/Button.jsx"
import { Button } from "shadcn-ui"

function Header() {
  return (
      <header>
          <div className="container">
              <a className="logo" href="/">
                  <img src="images/logo.jpg" id="logo" alt="LOGO"/>
              </a>
              <nav>
                  <ul>
                      <li>
                          <a href="#news">Yangiliklar</a>
                      </li>
                      <li>
                          <a href="#">Kutubxona haqida</a>
                      </li>
                      <li>
                          <a href="#contact">Bog'lanish</a>
                      </li>
                      <li>
                          <Button text={"O'rin band qilish"} color={"success"}/>
                      </li>
                  </ul>
              </nav>
          </div>
      </header>
  )
}

export default Header
