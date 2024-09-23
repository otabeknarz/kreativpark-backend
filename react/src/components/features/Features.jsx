import "./Features.css"

function Features() {
    return (
        <section id="features" className="features">
            <div className="container">
                <h3 className="top-title"><i className="fa-solid fa-circle-question"></i> Nimalar qilish mumkin</h3>
                <h1 className="heading">Siz Kreativ Parkda vaqtingizni aniq foydali ishlarga sarflaysiz</h1>
                <ul>
                    <li>
                        <div className="icon">
                            <img src="images/icons/palette.png" alt="Palette Icon"/>
                        </div>
                        <h1 className="title">Yaratish</h1>
                        <p className="subtitle">Qog’ozda rasm chizishga, planshet yoki noutbuklarda dizayn yaratishga
                            barcha imkoniyatlar mavjud, <span className="bold">IJOD QILING!</span></p>
                    </li>
                    <li>
                        <div className="icon">
                            <img src="images/icons/book.png" alt="Palette Icon"/>
                        </div>
                        <h1 className="title">Ilm olish</h1>
                        <p className="subtitle">Kitobxonmisiz? Kitob o’qish uchun <span
                            className="bold">aynan sizbop</span> joylar mavjud - yangi kitobxon <span className="bold">do’stlar orttiring</span> va
                            bilimingizni yana ham <span className="bold">charxlang</span></p>
                    </li>
                    <li>
                        <div className="icon">
                            <img src="images/icons/laptop-code.png" alt="Palette Icon"/>
                        </div>
                        <h1 className="title">Kompyuterda ishlash</h1>
                        <p className="subtitle">Albatta bu yerda ko’p insonlar kompyuterda ishlashadi <span
                            className="bold">siz ham</span> buni qila olasiz internet deysizmi? bizda <span
                            className="bold">bepul</span> internet mavjud</p>
                    </li>
                </ul>
            </div>
        </section>
    )
}

export default Features