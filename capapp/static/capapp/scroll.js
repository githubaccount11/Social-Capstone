
window.addEventListener("scroll", function() {
    // console.log(window.pageYOffset)
    window.localStorage.setItem('yScroll', window.pageYOffset)
})
// console.log(window.localStorage.getItem('yScroll'))
// console.log(typeof window.localStorage.getItem('yScroll'))
if (window.localStorage.getItem('lastUrl') == window.location.href) {
    window.scrollTo(0, Number(window.localStorage.getItem('yScroll')))
} else {
    window.localStorage.setItem('lastUrl', window.location.href)
}