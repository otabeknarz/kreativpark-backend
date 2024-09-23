import "./Stats.css"

function Stats() {
    return (
        <section className="stats" id="stats">
            <div className="container">
                <h3 className="top-title"><i className="fa-solid fa-chart-pie"></i> Statistika</h3>
                <h1 className="heading">Krativ Park raqamlarda</h1>
                <p className="subheading">Siz ham Kreativ Parkimizga tashrif buyurib vaqtingizni unumli sarflashingiz
                    mumkin</p>
                <ul>
                    <li>
                        <div className="icon">
                            <img src="images/icons/users.png" alt="Users Icon"/>
                        </div>
                        <p className="title">Kreativ Parkga umumiy kelganlar soni</p>
                        <h1 className="number">16 783</h1>
                    </li>
                    <li>
                        <div className="icon">
                            <img src="images/icons/latest.png" alt="Users Icon"/>
                        </div>
                        <p className="title">Hozirda Kreativ Parkda qancha odam bor</p>
                        <h1 className="number">433</h1>
                    </li>
                    <li>
                        <div className="icon">
                            <img src="images/icons/sofa.png" alt="Users Icon"/>
                        </div>
                        <p className="title">Hozirgi vaqtdagi barcha bo’sh o’rinlar soni</p>
                        <h1 className="number">37</h1>
                    </li>
                </ul>
            </div>
        </section>
    )
}

export default Stats;