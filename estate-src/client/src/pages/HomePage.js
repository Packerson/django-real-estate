import React from "react";
import About from '../components/home/About'
import Banner from '../components/home/Banner'
import Options from '../components/home/Options'
import Faqs from '../components/home/Faqs'

function HomePage() {
    return (
        <div className="main">
            <Banner/>
            <About/>
            <Options/>
            <Faqs/>
        </div>
    );
}

export default HomePage;
