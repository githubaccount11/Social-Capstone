
window.addEventListener("scroll", function() {
    // console.log(window.pageYOffset)
    window.localStorage.setItem('yScroll', window.pageYOffset)
})
// console.log(window.localStorage.getItem('yScroll'))
// console.log(typeof window.localStorage.getItem('yScroll'))
window.scrollTo(0, Number(window.localStorage.getItem('yScroll')))