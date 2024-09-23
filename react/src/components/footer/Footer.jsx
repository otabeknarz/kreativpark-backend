import "./Footer.css";

function Footer() {
    return (
        <footer id="footer">
            <div className="container">
                <div className="logo">
                    <h1>Kreativ Park</h1>
                    <div className="social-medias">
                        <a href="#">
                            <i style={{ color: 'orangered' }} className="fa-brands fa-instagram"></i> <span>Instagram</span>
                        </a>
                        <a href="https://t.me/kreativparkuz">
                            <i style={{ color: 'dodgerblue' }} className="fa-brands fa-telegram"></i> <span>Telegram</span>
                        </a>
                        <a href="https://t.me/kreativpark_bot">
                            <i className="fa-solid fa-robot"></i> <span>Telegram Bot</span>
                        </a>
                    </div>
                </div>
                <ul>
                    <li className="title">
                        1-qavat
                    </li>
                    <li>
                        <a href="#">Post</a>
                    </li>
                    <li>
                        <a href="#">Ijod books</a>
                    </li>
                    <li>
                        <a href="#">Xojatxona</a>
                    </li>
                </ul>
                <ul>
                    <li className="title">
                        2-qavat
                    </li>
                    <li>
                        <a href="#">Ibrat Farzandlari</a>
                    </li>
                    <li>
                        <a href="#">Kutubxona</a>
                    </li>
                    <li>
                        <a href="#">Ijod Cafe</a>
                    </li>
                </ul>
            </div>
        </footer>
    );
}

export default Footer;
