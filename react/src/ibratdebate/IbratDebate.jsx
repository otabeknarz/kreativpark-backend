import "./IbratDebate.css"
import { motion } from "framer-motion"

function IbratDebate() {
    return (
        <div className="IbratDebate">
            <div className="container">
                <motion.div
                    initial={{
                        opacity: 0.3,
                    }}
                    whileInView={{
                        opacity: 1,
                    }}
                    viewport={{
                        amount: "all",
                    }}
                    className="debate-first">
                    <img src="images/ibratdebate/1.png" alt="IbratDebate"/>
                    <div className="description">
                        <h1 className="title" style={{color: "#FF9721"}}>Ibrat Debate</h1>
                        <p className="info" style={{color: "#656565"}}>
                            @ibratfarzandlari tomonidan tashkil etilgan <br/> <br/>
                            “Ibrat Debate” - yurtimizning turli xil hududlarida tilida debate sessiyalari <br/> <br/>
                            <a href="https://otabek.me" target="_blank">Ibrat Debate sayti</a>
                        </p>
                        <div className="register-btn">
                            <a className="btn-primary" target="_blank" style={{backgroundColor: "#FF9721"}}
                               href="https://t.me/ibratdebate_bot">Debate ga ro’yxatdan o’tish
                            </a>
                        </div>
                    </div>
                </motion.div>
                <div className="debate-second">
                    <div className="description">
                        <h1 className="title" style={{color: "#FF9721"}}>Ibrat Debate</h1>
                        <p className="info" style={{color: "#656565"}}>
                            Speaking ni oshirmoqchisiz nima qilishni bilmaysizmi? <br/>
                            Debate lar aynan siz uchun - siz uchun qulay vaqtda <br/>
                            Debate larda o’zingiz kabi tengdoshlar bilan tanishib networkingni kuchaytiring - kreativ odamlar bilan tanishing
                        </p>
                    </div>
                    <div className="images">
                        <img src="images/ibratdebate/2.png" alt="Ibrat Debate"/>
                        <img src="images/ibratdebate/3.png" alt="Ibrat Debate"/>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default IbratDebate