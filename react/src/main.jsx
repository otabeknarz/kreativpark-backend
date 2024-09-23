import { createRoot } from 'react-dom/client'
import Header from './components/header/Header.jsx'
import Footer from './components/footer/Footer.jsx'
import IbratDebate from "./ibratdebate/IbratDebate.jsx";
import Index from "./components/index/Index.jsx";
import Features from "./components/features/Features.jsx";
import News from "./components/News/News.jsx";
import Stats from "./components/Stats/Stats.jsx";
import Contacts from "./components/Contacts/Contacts.jsx";
import './index.css'

createRoot(document.getElementById('root')).render(
    <>
        <Header />
        <Index />
        <Features />
        <News />
        <Stats />
        <IbratDebate />
        <Contacts />
        <Footer />
    </>
)
