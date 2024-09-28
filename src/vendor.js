import Alpine from 'alpinejs';
import '../node_modules/lite-youtube-embed/src/lite-yt-embed.css';
import '../node_modules/lite-youtube-embed/src/lite-yt-embed.js';
import './scss/styles.scss';
// import Swiper from 'swiper';
// import { Autoplay, Navigation, Pagination, EffectCards } from 'swiper/modules';
// import 'swiper/css';
// import 'swiper/css/effect-cards';
import CustomToast from "./toast";
// import { register as swipperRegister  } from 'swiper/element/bundle';
window.htmx = require('htmx.org');

document.addEventListener('display_toast', (e) => {
  CustomToast({template_id:"toast-template", data:e.detail})
});

document.addEventListener("DOMContentLoaded", () => {
    window.Alpine = Alpine;
    Alpine.start();

    // swipperRegister();

    // // testimonial swipper
    // const progressCircle = document.querySelector(".autoplay-progress svg");
    // const progressContent = document.querySelector(".autoplay-progress span");

    // const swiper = new Swiper('#testimonial-wrapper', {
    //     modules: [Autoplay, Navigation, Pagination],

    //     // Optional parameters
    //     loop: true,
    //     speed: 1000,

    //     slidesPerView: 1,
    //     breakpoints: {
    //       1024: {
    //         slidesPerView: 2,
    //       },
        
    //     },
    //     autoplay: {
    //         delay: 8000,
    //         disableOnInteraction: false,
    //     },
    //     on: {
    //         autoplayTimeLeft(s, time, progress) {
    //           progressCircle.style.setProperty("--progress", 1 - progress);
    //           progressContent.textContent = `${Math.ceil(time / 1000)}s`;
    //         }
    //       }

    // });
    

});