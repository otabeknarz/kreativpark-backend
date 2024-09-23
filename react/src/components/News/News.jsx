import "./News.css";
// Import Swiper React components
import { Navigation, Pagination, A11y } from 'swiper/modules';
import { Swiper, SwiperSlide } from 'swiper/react';

// Import Swiper styles
import 'swiper/css/bundle';

function News() {
    return (
        <section className="news container" id="news">
            <h1><i className="fa-solid fa-newspaper"></i> Yangiliklar</h1>
            <div className="slider swiper">
                <div className="swiper-wrapper">
                    <Swiper
                      modules={[Navigation, Pagination, A11y ]}
                      breakpoints={{
                      640: {
                        slidesPerView: 1,
                        spaceBetween: 20,
                      },
                      768: {
                        slidesPerView: 2,
                        spaceBetween: 40,
                      },
                      1024: {
                        slidesPerView: 3,
                        spaceBetween: 50,
                      },
                    }}
                      navigation
                      loop={true}
                      pagination={{ clickable: true }}
                    >
                        <SwiperSlide className="swiper-slide card">
                            <div className="image">
                                <img className="view-image" src="https://picsum.photos/800" alt="Image"/>
                                <i className="fa-solid fa-eye"></i>
                            </div>
                            <div className="top">
                                <p className="date"><i className="fa-solid fa-calendar-days"></i> 11/04</p>
                                <div className="views">
                                    <i className="fa-solid fa-eye"></i> 10
                                </div>
                            </div>
                            <a className="info" href="">
                                <h2 className="title">Title goes here</h2>
                                <p className="subtitle">Description goes here</p>
                            </a>
                        </SwiperSlide>
                        <SwiperSlide className="swiper-slide card">
                            <div className="image">
                                <img className="view-image" src="https://picsum.photos/800" alt="Image"/>
                                <i className="fa-solid fa-eye"></i>
                            </div>
                            <div className="top">
                                <p className="date"><i className="fa-solid fa-calendar-days"></i> 11/04</p>
                                <div className="views">
                                    <i className="fa-solid fa-eye"></i> 10
                                </div>
                            </div>
                            <a className="info" href="">
                                <h2 className="title">Title goes here</h2>
                                <p className="subtitle">Description goes here</p>
                            </a>
                        </SwiperSlide>
                        <SwiperSlide className="swiper-slide card">
                            <div className="image">
                                <img className="view-image" src="https://picsum.photos/800" alt="Image"/>
                                <i className="fa-solid fa-eye"></i>
                            </div>
                            <div className="top">
                                <p className="date"><i className="fa-solid fa-calendar-days"></i> 11/04</p>
                                <div className="views">
                                    <i className="fa-solid fa-eye"></i> 10
                                </div>
                            </div>
                            <a className="info" href="">
                                <h2 className="title">Title goes here</h2>
                                <p className="subtitle">Description goes here</p>
                            </a>
                        </SwiperSlide>
                        <SwiperSlide className="swiper-slide card">
                            <div className="image">
                                <img className="view-image" src="https://picsum.photos/800" alt="Image"/>
                                <i className="fa-solid fa-eye"></i>
                            </div>
                            <div className="top">
                                <p className="date"><i className="fa-solid fa-calendar-days"></i> 11/04</p>
                                <div className="views">
                                    <i className="fa-solid fa-eye"></i> 10
                                </div>
                            </div>
                            <a className="info" href="">
                                <h2 className="title">Title goes here</h2>
                                <p className="subtitle">Description goes here</p>
                            </a>
                        </SwiperSlide>
                        <SwiperSlide className="swiper-slide card">
                            <div className="image">
                                <img className="view-image" src="https://picsum.photos/800" alt="Image"/>
                                <i className="fa-solid fa-eye"></i>
                            </div>
                            <div className="top">
                                <p className="date"><i className="fa-solid fa-calendar-days"></i> 11/04</p>
                                <div className="views">
                                    <i className="fa-solid fa-eye"></i> 10
                                </div>
                            </div>
                            <a className="info" href="">
                                <h2 className="title">Title goes here</h2>
                                <p className="subtitle">Description goes here</p>
                            </a>
                        </SwiperSlide>
                        <SwiperSlide className="swiper-slide card">
                            <div className="image">
                                <img className="view-image" src="https://picsum.photos/800" alt="Image"/>
                                <i className="fa-solid fa-eye"></i>
                            </div>
                            <div className="top">
                                <p className="date"><i className="fa-solid fa-calendar-days"></i> 11/04</p>
                                <div className="views">
                                    <i className="fa-solid fa-eye"></i> 10
                                </div>
                            </div>
                            <a className="info" href="">
                                <h2 className="title">Title goes here</h2>
                                <p className="subtitle">Description goes here</p>
                            </a>
                        </SwiperSlide>
                    </Swiper>

                </div>

            </div>
        </section>
    );
}

export default News;
