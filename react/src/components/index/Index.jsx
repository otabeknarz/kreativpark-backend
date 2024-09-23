import "./Index.css"

function Index() {
    return (
        <section className="welcome" id="welcome">
            <img id="welcome-image" src="images/core/home/welcome-image.jpg" alt="WELCOME-IMAGE"/>
            <div className="welcome-text">
                <h1>Kreativ Park - o'zingiz xoxlagan joyingizni band qiling</h1>
                <a href="#" className="btn-primary">Joy band qilish</a>
            </div>
        </section>
    )
}

export default Index